import { useState } from "react";
import Simulation from "../components/Simulation";

const Calculator = () => {
  const getSquare = (n: number) => n ** 2;

  const [particleCount, setParticleCount] = useState(40);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setParticleCount(Number(e.target.value));
  };
  return (
    <div className="w-screen h-screen flex flex-col">
      <div className="flex-1">
        <Simulation particleCount={getSquare(particleCount)} />
      </div>
      <div className="flex gap-2">
        {/*TODO: look into React Slider, this doesn't have good UX for quadratic mapping*/}
        <input
          role="slider"
          type="range"
          min="0"
          max="100"
          step="1"
          value={particleCount}
          onChange={handleChange}
        />
        <span className="text-lg">{getSquare(particleCount)}</span>
      </div>
    </div>
  );
};

export default Calculator;
