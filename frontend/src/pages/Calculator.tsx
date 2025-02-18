import { useState } from "react";
import Simulation from "../components/Simulation";

const Calculator = () => {
  const getSquare = (n: number) => n ** 2;

  const [index, setIndex] = useState(1);
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setIndex(Number(e.target.value));
  };
  return (
    <div className="w-screen h-screen flex flex-col">
      <div className="flex-1">
        <Simulation />
      </div>
      <div className="flex gap-2">
        <input
          role="slider"
          type="range"
          min="0"
          max="100"
          step="1"
          value={index}
          onChange={handleChange}
        />
        <span className="text-lg">{getSquare(index)}</span>
      </div>
    </div>
  );
};

export default Calculator;
