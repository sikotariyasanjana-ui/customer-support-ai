# Deployment Guide: Customer Support AI 🚀

This guide provides step-by-step instructions to deploy the database, backend, and frontend of the Customer Support AI application.

---

## 1. MongoDB Atlas Setup (Cloud Database)

MongoDB Atlas is the cloud version of MongoDB. To set up your database:

1. **Sign Up / Log In**: Visit [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) and sign up or log in.
2. **Create a Free Cluster**: 
   - Click **Create** to deploy a new database.
   - Choose the **M0 (Free)** cluster tier.
   - Choose your preferred cloud provider (e.g. AWS) and region (e.g. closest to you).
   - Click **Create**.
3. **Database User Credentials**:
   - In the "Security Quickstart" screen, create a database username (e.g., `sikotariyasanjana_db_user`) and a secure password.
   - **Save these credentials** as they will form part of your connection URI.
4. **IP Access List Configuration**:
   - Under "Where would you like to connect from?", select **Cloud Environment**.
   - To deploy securely, you should allow connections from anywhere since cloud deployment IPs change dynamically: add `0.0.0.0/0` (allow access from anywhere) to the IP access list.
   - Click **Add Entry**.
5. **Get Connection String**:
   - Go to the Atlas Dashboard -> **Database** tab.
   - Click **Connect** on your cluster.
   - Choose **Drivers** under "Connect your application".
   - Copy the connection string. It will look like this:
     ```text
     mongodb+srv://sikotariyasanjana_db_user:<db_password>@cluster0.ljzjoni.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
     ```
   - Replace `<db_password>` with the password you created in step 3.

---

## 2. Gemini API Key Creation

To allow the chatbot to generate replies using Google Gemini:

1. **AI Studio Login**: Visit [Google AI Studio](https://aistudio.google.com/).
2. **Get API Key**:
   - Click the **Get API Key** button in the top-left menu.
   - Click **Create API Key**.
   - You can choose to create a key in a new project or an existing project.
   - Copy the generated API key (it starts with `AIzaSy...`).
   - Save this key securely.

---

## 3. Backend Deployment (Render or Railway)

### Option A: Deploying on Render (Recommended Free Tier)

1. **Sign Up / Log In**: Log in to [Render](https://render.com/).
2. **Create Web Service**:
   - Click **New +** -> **Web Service**.
   - Connect your GitHub Repository containing the `customer-support-ai` code.
3. **Configure Settings**:
   - **Name**: `customer-support-ai-backend`
   - **Root Directory**: `backend` (CRITICAL: set this so Render looks inside the backend folder)
   - **Language/Runtime**: `Python`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
4. **Set Environment Variables**:
   - Click the **Environment** tab on Render.
   - Add the following variables:
     - `MONGO_URI`: (Your MongoDB Atlas connection string from Section 1)
     - `DATABASE_NAME`: `customer_support_ai`
     - `GEMINI_API_KEY`: (Your Google Gemini API Key from Section 2)
     - `ALLOWED_ORIGINS`: `*` (or your frontend Vercel URL after it's deployed to restrict CORS)
5. **Deploy**: Click **Create Web Service** to start the build. Once completed, copy the generated service URL (e.g., `https://customer-support-ai-backend.onrender.com`).

---

### Option B: Deploying on Railway

1. **Sign Up / Log In**: Log in to [Railway](https://railway.app/).
2. **Create New Project**:
   - Click **New Project** -> **Deploy from GitHub repo**.
   - Choose your repository.
3. **Configure Root Directory and Variables**:
   - Go to settings of the service, set **Root Directory** to `backend`.
   - Add variables:
     - `MONGO_URI`
     - `DATABASE_NAME`
     - `GEMINI_API_KEY`
     - `ALLOWED_ORIGINS` (e.g., `*`)
4. **Deploy**: Railway will read the `Procfile` inside the `backend` folder and deploy automatically. Copy the public domain URL once generated.

---

## 4. Frontend Deployment (Vercel)

Vercel is the easiest place to host your React (Vite) frontend.

1. **Sign Up / Log In**: Log in to [Vercel](https://vercel.com/).
2. **Import Project**:
   - Click **Add New** -> **Project**.
   - Import your GitHub repository.
3. **Configure Project Settings**:
   - **Framework Preset**: `Vite` (automatically detected)
   - **Root Directory**: `frontend` (CRITICAL: set this so Vercel builds the React frontend)
4. **Configure Environment Variables**:
   - Expand the **Environment Variables** section.
   - Add the following variable:
     - **Key**: `VITE_API_URL`
     - **Value**: `https://<your-backend-domain>.onrender.com/api` (Replace with your actual deployed Backend URL, appending `/api` at the end)
5. **Deploy**:
   - Click **Deploy**. Vercel will build the frontend and serve it.
   - If you refresh any subpages (like `/chat` or `/history`), the custom `vercel.json` we created will redirect traffic to `/index.html` to prevent any 404 errors.
