import React, { useState } from "react";
import "./App.css";
import "@fontsource/roboto/300.css";
import "@fontsource/roboto/400.css";
import "@fontsource/roboto/500.css";
import "@fontsource/roboto/700.css";
import { Routes, Route } from "react-router-dom";
import Homepage from "./Pages/Homepage";
import Header from "./NavCompnents/Header";

function App() {
  return (
    <>
      <div className="app_container">
        <Header />
        <div className="header_spacer" />
        <Routes>
          <Route path="/" element={<Homepage />} />
        </Routes>
      </div>
    </>
  );
}

export default App;
