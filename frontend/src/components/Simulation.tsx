import { PointMaterial, Points } from "@react-three/drei";
import { Canvas, useFrame } from "@react-three/fiber";
import React, { useEffect, useMemo } from "react";
import * as THREE from "three";

type ParticleSystemProps = {
  particleCount: number;
  setLatLonArr: (num: Float32Array) => void;
};
const ParticleSystem: React.FC<ParticleSystemProps> = ({
  particleCount,
  setLatLonArr,
}) => {
  //TODO: fix that type
  const particleRef = React.useRef<THREE.Points>(null);

  useEffect(() => {
    return () => {
      if (particleRef.current) particleRef.current.geometry.dispose();
    };
  }, [particleCount]);

  const positions = useMemo(() => {
    const cartesian = new Float32Array(particleCount * 3);
    const latLon = new Float32Array(particleCount * 2);

    // NOTE: apparently evenly spaced points on a sphere is a tough problem!!! look more into this later!
    for (let i = 0; i < particleCount; i++) {
      const y = 1 - (i / (particleCount - 1)) * 2;
      const radius = Math.sqrt(1 - y * y);
      const phi = i * Math.PI * (3 - Math.sqrt(5));

      const x = Math.cos(phi) * radius * 2;
      const z = Math.sin(phi) * radius * 2;

      cartesian[i * 3] = x;
      cartesian[i * 3 + 1] = y * 2;
      cartesian[i * 3 + 2] = z;

      latLon[i * 2] = Math.asin((y * 2) / 2) * (180 / Math.PI); //lat
      latLon[i * 2 + 1] = Math.atan2(z, x) * (180 / Math.PI); //lon
    }
    setLatLonArr(latLon);
    return { cartesian, latLon };
  }, [particleCount, setLatLonArr]);

  useFrame((_, delta) => {
    particleRef.current!.rotation.x += delta / 10;
    particleRef.current!.rotation.y += delta / 15;
  });

  return (
    <Points
      ref={particleRef}
      positions={positions.cartesian}
      stride={3}
      frustumCulled={false}
    >
      <PointMaterial
        transparent
        color="#341539"
        size={0.02}
        sizeAttenuation={true}
        depthWrite={false}
      />
    </Points>
  );
};

type SimulationProps = {
  particleCount: number;
  setLatLonArr: (num: Float32Array) => void;
};

const Simulation: React.FC<SimulationProps> = ({
  particleCount,
  setLatLonArr,
}) => {
  return (
    <Canvas camera={{ position: [0, 0, 5], fov: 75 }}>
      <ParticleSystem
        particleCount={particleCount}
        setLatLonArr={setLatLonArr}
      />
    </Canvas>
  );
};

export default Simulation;
