import { PointMaterial, Points } from "@react-three/drei";
import { Canvas, useFrame } from "@react-three/fiber";
import React, { useMemo } from "react";
import * as THREE from "three";

function ParticleSystem() {
  const count = 10000;
  const positions = useMemo(() => {
    const pos = new Float32Array(count * 3);
    for (let i = 0; i < count; i++) {
      const theta = THREE.MathUtils.randFloatSpread(2 * Math.PI);
      const phi = THREE.MathUtils.randFloatSpread(2 * Math.PI);

      pos[i * 3] = Math.sin(theta) * Math.cos(phi) * 2;
      pos[i * 3 + 1] = Math.sin(phi) * 2;
      pos[i * 3 + 2] = Math.cos(theta) * Math.cos(phi) * 2;
    }
    return pos;
  }, [count]);

  //TODO: fix that type
  const particleRef = React.useRef<THREE.Points>(null);

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
}

const Simulation = () => {
  return (
    <Canvas camera={{ position: [0, 0, 5], fov: 75 }}>
      <ParticleSystem />
    </Canvas>
  );
};

export default Simulation;
