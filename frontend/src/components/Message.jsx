function Message({ sender, text }) {

    return (

        <div
            style={{
                margin: "10px",
                textAlign: sender === "user" ? "right" : "left",
            }}
        >

            <span
                style={{
                    background: sender === "user" ? "#2563eb" : "#e5e7eb",
                    color: sender === "user" ? "white" : "black",
                    padding: "10px",
                    borderRadius: "10px",
                    display: "inline-block",
                    maxWidth: "70%",
                }}
            >
                {text}
            </span>

        </div>

    );

}

export default Message;