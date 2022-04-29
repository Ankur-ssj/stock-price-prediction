import React, { Suspense, useMemo, useCallback, useRef } from 'react';
import * as THREE from 'three';
/* import {Button} from './Button'
import {Link} from 'react-router-dom' */
import {gsap} from 'gsap';
import {ScrollTrigger} from 'gsap/ScrollTrigger'
import {Canvas, useFrame, useLoader} from '@react-three/fiber';
import Ellipse from '../Images/Ellipse.png'
import '../Scss/Workspace.css'

gsap.registerPlugin(ScrollTrigger);

function Points(){
    const imgTex = useLoader(THREE.TextureLoader, Ellipse);
    const bufferRef = useRef();
    let t = 0;
    let f = 0.0025;
    let a = 1.2;
    const graph = useCallback(
        (x, z) => {
            return Math.sin(f * (x ** 2 + z ** 2 + t)) * a;
        },
        [t, f, a],
    )

    const count = 30
    const sep = 15.5
    let positions = useMemo(() => {
      let positions = []
  
      for (let xi = 0; xi < count; xi++) {
        for (let zi = 0; zi < count; zi++) {
          let x = sep * (xi - count / 2);
          let z = sep * (zi - count / 2);
          let y = graph(x, z);
          positions.push(x, y, z);
        }
      }
  
      return new Float32Array(positions);
    }, [count, sep, graph])

    useFrame(()=> {
        t += 14
        const positions = bufferRef.current.array;

        let i = 0;
        for (let xi = 0; xi < count; xi++) {
            for (let zi = 0; zi < count; zi++) {
              let x = sep * (xi - count / 2);
              let z = sep * (zi - count / 2);
              
              positions[i + 1] = graph(x, z);
              i += 3;
            }
          }

        bufferRef.current.needsUpdate = true;
    })

    return(
        <points>
        <bufferGeometry attach="geometry">
          <bufferAttribute
            ref={bufferRef}
            attachObject={['attributes', 'position']}
            array={positions}
            count={positions.length / 3}
            itemSize={3}
          />
        </bufferGeometry>
  
        <pointsMaterial
          attach="material"
          map={imgTex}
          size={0.85}
          sizeAttenuation
          transparent={false}
          alphaTest={0.5}
          opacity={1.0}
        />
      </points>
    ); 
}

function AnimationCanvas(){
    return(
        <Canvas
            colorManagement = {false}
            camera = {{position: [100, 1.5, 25.5], fov: 75, near: 0.01}}
        >
            <Suspense fallback={null}>
                <Points/>
            </Suspense>

        </Canvas>
    );
}

function WavePraticles(){

    const revealRefs = useRef(null); 
    revealRefs.current = [];

/*     useEffect(() => {

        revealRefs.current.forEach((el, index) =>{
            gsap.fromTo(el, {
                autoAlpha: 0
            }, {
                duration: 1, 
                autoAlpha: 1, 
                ease: 'none',
                scrollTrigger: {
                    id: `sections-${index+1}`,
                    trigger: el,
                    start: 'top center+=1000',
                    toggleActions: 'play none none reverse',
                    markers: true
                }
            })
        });
    }, []) */

    const addToRefs = (el) => {
        if(el && !revealRefs.current.includes(el)){
            revealRefs.current.push(el);
        }
        console.log(revealRefs.current);
    };

    return (
        <div className="wrapper">
            <div className="anim">
                <Suspense className="object" fallback={<div>Loading...</div>}>
                    <AnimationCanvas />
                </Suspense>
            </div>
        </div> 
    )
}

export default WavePraticles
   