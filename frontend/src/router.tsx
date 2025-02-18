import { Route, Routes } from "react-router-dom";
import Calculator from "./pages/Calculator";

const RouterComponent = () => {
  return (
    <Routes>
      <Route path="/" element={<Calculator />}></Route>
    </Routes>
  );
};

export default RouterComponent;
