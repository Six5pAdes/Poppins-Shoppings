import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getUserHistoryThunk } from "../../redux/history";
// import './OrderHistory.css'

const OrderHistory = () => {
    const dispatch = useDispatch();
    const histories = useSelector(state => state.history?.UserOrderHistory);
    const products = useSelector(state => state.history?.HistoryProd)

    const allHistory = histories?.map(order =>
        order = {
            ...order, "product": products?.filter(product => product.id == order.product_id)[0]
        }
    )

    const sortHistory = allHistory?.reduce((acc, order) => {
        const createdAt = order.createdAt?.slice(0, 16)
        if (!acc[createdAt]) {
            acc[createdAt] = []
        }
        acc[createdAt].push(order)
        return acc
    }, {})

    let historySorted = []
    if (sortHistory) {
        historySorted = Object.values(sortHistory)
    }

    const getTotal = (history) => {
        const total = history.reduce((acc, order) => {
            const price = order.product?.price * order.quantity
            return acc + price
        }, 0)
        return total
    }

    useEffect(() => {
        dispatch(getUserHistoryThunk())
    }, [dispatch])

    return (
        <div className='order-history-contain'>
            <h1 id='curr-title'>Order History</h1>
            <div id='order-history'>
                {historySorted?.reverse().map((historyArr) => (
                    <div className="history-head" key={historyArr[0].createdAt}>
                        <div>
                            <h2>{historyArr[0]?.createdAt?.slice(0, 16).split(' ')[0]}</h2>
                            <h3>{historyArr[0]?.createdAt?.slice(0, 16).split(' ')[1]}</h3>
                        </div>
                        <h3 className='history-subtotal'>Subtotal: {getTotal(historyArr)}</h3>
                        {history?.map((order) => (
                            <div key={order.id} className='order-history'>
                                <img src={order.product.image} alt={order.product.name} />
                                <h3>{order.product.name}</h3>
                                <h4>Quantity: {order.quantity}</h4>
                                <h4>Price: ${order.product.price}</h4>
                                <h4>Total: ${order.product.price * order.quantity}</h4>
                            </div>
                        ))}
                    </div>
                ))}
            </div>
        </div>
    )
}

export default OrderHistory;