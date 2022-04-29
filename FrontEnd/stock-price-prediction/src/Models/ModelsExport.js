import React, {Suspense} from 'react'
import {Canvas} from '@react-three/fiber'
import { Html, useProgress, OrbitControls} from '@react-three/drei';

const Graph = React.lazy(() => import('./Graph'))


function Loader() {
    const { progress } = useProgress()
    return <Html center>{progress} % loaded</Html>
}

export const GraphModel = () => {
  return (
    <>
     <Canvas concurrent camera={{ position: [1, 1.5, 25.5], fov: 75, near: 0.01 }}>
                <ambientLight/>
                <OrbitControls autoRotate enablePan={false} enableZoom={false} minPolarAngle={Math.PI / 2.2} maxPolarAngle={Math.PI / 2.2}/>
                <directionalLight intensity={1} position={[5, 8, 8]} castShadow shadow-mapSize-width={1024} shadow-mapSize-height={1024} 
                    shadow-camera-far={50}
                    shadow-camera-left = {-10}
                    shadow-camera-right = {10}
                    shadow-camera-top = {20}
                    shadow-camera-bottom = {-20} />
                <group position={[0, -1, 0]}>
                <Suspense fallback={<Loader/>}>
                    <Graph/>
                </Suspense>
                </group>
            </Canvas>
    </>
  )
}
