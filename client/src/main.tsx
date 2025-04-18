import React from "react";

import ReactDOM from "react-dom/client";
import "./utils/i18n.ts";

import App from "./App.tsx";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
