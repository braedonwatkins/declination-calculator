import { ToastContainer } from "react-toastify";
import RouterComponent from "./router";

const App = () => {
  return (
    <div className="h-screen w-screen flex flex-col">
      <ToastContainer />
      <RouterComponent />
    </div>
  );
};

export default App;
