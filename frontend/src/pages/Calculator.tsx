import { useState } from "react";
import Simulation from "../components/Simulation";
import { toast } from "react-toastify";
import handleAxiosError from "../utils/handleAxiosError";
import axios from "axios";

const Calculator = () => {
  const getSquare = (n: number) => n ** 2;

  const [particleCount, setParticleCount] = useState(40);
  const [latLonArr, setLatLonArr] = useState<Float32Array>(new Float32Array());

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setParticleCount(Number(e.target.value));
  };

  const getVectorField = async (latLonArr: Float32Array) => {
    try {
      toast.info("Calculating Vector Field");
      //TODO: const URL, h, and year
      await axios.post(`http://localhost:8000/vector-field`, {
        lat_lon_list: Array.from(latLonArr), //TODO: figure out if this is bad for perf?
        h: 0.0,
        year: 2025.0,
      });

      //TODO: ideally we dont toast this but just render results
      toast.success("Vector Field Calculated");
    } catch (err: unknown) {
      handleAxiosError(err, "Get Vector Field");
    }
  };

  return (
    <div className="w-screen h-screen flex flex-col">
      <div className="flex-1 overflow-hidden">
        <Simulation
          particleCount={getSquare(particleCount)}
          setLatLonArr={setLatLonArr}
        />
      </div>
      <div className="flex items-center h-20 gap-2 py-2 pb-1">
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
        <button
          className="bg-blue-500 text-white px-2 py-1 rounded transition-transform duration-100 hover:bg-blue-600 active:scale-95"
          onClick={() => {
            getVectorField(latLonArr);
          }}
        >
          Submitty
        </button>
      </div>
    </div>
  );
};

export default Calculator;
