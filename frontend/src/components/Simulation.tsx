import { PointMaterial, Points } from "@react-three/drei";
import { Canvas, useFrame } from "@react-three/fiber";
import React, { useEffect, useMemo } from "react";
import * as THREE from "three";

type ParticeSystemProps = {
  particleCount: number;
};
const ParticleSystem: React.FC<ParticeSystemProps> = ({ particleCount }) => {
  //TODO: fix that type
  const particleRef = React.useRef<THREE.Points>(null);

  useEffect(() => {
    return () => {
      if (particleRef.current) particleRef.current.geometry.dispose();
    };
  }, [particleCount]);

  const positions = useMemo(() => {
    const pos = new Float32Array(particleCount * 3);
    const latLonArray = new Float32Array(particleCount * 2);

    // NOTE: apparently evenly spaced points on a sphere is a tough problem!!! look more into this later!
    for (let i = 0; i < particleCount; i++) {
      const y = 1 - (i / (particleCount - 1)) * 2;
      const radius = Math.sqrt(1 - y * y);
      const phi = i * Math.PI * (3 - Math.sqrt(5));

      const x = Math.cos(phi) * radius * 2;
      const z = Math.sin(phi) * radius * 2;

      pos[i * 3] = x;
      pos[i * 3 + 1] = y * 2;
      pos[i * 3 + 2] = z;

      latLonArray[i * 2] = Math.asin((y * 2) / 2) * (180 / Math.PI);
      latLonArray[i * 2 + 1] = Math.atan2(z, x) * (180 / Math.PI);
    }
    return pos;
  }, [particleCount]);

  useFrame((_, delta) => {
    particleRef.current!.rotation.x += delta / 10;
    particleRef.current!.rotation.y += delta / 15;
  });

  return (
    <Points
      ref={particleRef}
      positions={positions}
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
};

const Simulation: React.FC<SimulationProps> = ({ particleCount }) => {
  return (
    <Canvas camera={{ position: [0, 0, 5], fov: 75 }}>
      <ParticleSystem particleCount={particleCount} />
    </Canvas>
  );
};

export default Simulation;
