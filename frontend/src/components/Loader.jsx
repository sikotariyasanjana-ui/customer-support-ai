import "../styles/app.css";

function Loader() {

    return (

        <div
            style={{
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
                height: "200px",
                fontSize: "22px",
                fontWeight: "bold",
            }}
        >
            Loading...
        </div>

    );

}

export default Loader;