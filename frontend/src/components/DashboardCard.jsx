import "../styles/home.css";

function DashboardCard({ title, description, icon }) {

    return (

        <div className="card">

            <h2>{icon}</h2>

            <h3>{title}</h3>

            <p>{description}</p>

        </div>

    );

}

export default DashboardCard;