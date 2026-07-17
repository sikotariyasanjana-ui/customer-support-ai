import Sidebar from "../components/Sidebar";
import DashboardCard from "../components/DashboardCard";
import "../styles/home.css";

function Home() {
    return (
        <div className="home-container">
            <Sidebar />

            <div className="home-content">

                <h1 className="dashboard-title">
                    Customer Support AI Dashboard
                </h1>

                <p className="dashboard-subtitle">
                    Welcome to the AI-powered Customer Support System.
                </p>

                <div className="dashboard-grid">

                    <DashboardCard
                        icon="💳"
                        title="Billing Support"
                        description="Handle invoices, payments and billing queries."
                    />

                    <DashboardCard
                        icon="🛠"
                        title="Technical Support"
                        description="Resolve technical issues and troubleshooting."
                    />

                    <DashboardCard
                        icon="📦"
                        title="Product Information"
                        description="Provide product details and recommendations."
                    />

                    <DashboardCard
                        icon="⚠"
                        title="Complaint Support"
                        description="Track and resolve customer complaints."
                    />

                    <DashboardCard
                        icon="❓"
                        title="FAQ Assistant"
                        description="Answer frequently asked customer questions."
                    />

                    <DashboardCard
                        icon="🤖"
                        title="AI Chatbot"
                        description="24×7 intelligent customer support."
                    />

                </div>

            </div>
        </div>
    );
}

export default Home;