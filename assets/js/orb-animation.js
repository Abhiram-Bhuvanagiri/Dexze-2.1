import React, { useState, useEffect, useRef, useLayoutEffect } from 'react';
import { createRoot } from 'react-dom/client';
import { motion, useAnimation } from 'framer-motion';

const PremiumOrb = () => {
  const containerRef = useRef(null);
  const orbRef = useRef(null);
  const shadowRef = useRef(null);
  const parallaxRef = useRef(null);
  const [isEntranceComplete, setIsEntranceComplete] = useState(false);

  // Responsive values
  const [orbSize, setOrbSize] = useState(220);
  const [isMobile, setIsMobile] = useState(false);

  useLayoutEffect(() => {
    const handleResize = () => {
      if (window.innerWidth <= 767) {
        setOrbSize(200); // Increased mobile
        setIsMobile(true);
      } else if (window.innerWidth <= 1024) {
        setOrbSize(260); // Increased tablet
        setIsMobile(false);
      } else {
        setOrbSize(340); // Increased desktop
        setIsMobile(false);
      }
    };
    handleResize();
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);

  // Entrance Animation (GSAP + ScrollTrigger)
  useEffect(() => {
    const gsap = window.gsap;
    const ScrollTrigger = window.ScrollTrigger;
    
    if (!gsap || !ScrollTrigger) return;
    
    gsap.registerPlugin(ScrollTrigger);

    // Initial hidden state
    gsap.set([orbRef.current, shadowRef.current], { 
      autoAlpha: 0,
      scale: 0.82, 
      y: 60, 
      rotationZ: -8 
    });

    const st = ScrollTrigger.create({
      trigger: containerRef.current,
      start: "top 70%", // Triggers when 70% of section becomes visible roughly
      once: true,
      onEnter: () => {
        gsap.to([orbRef.current, shadowRef.current], {
          autoAlpha: 1,
          scale: 1,
          y: 0,
          rotationZ: 0,
          duration: 1.4,
          ease: "power4.out",
          delay: 0.15,
          onComplete: () => {
            // Clean up GSAP transform and opacity inline styles to avoid conflict
            gsap.set([orbRef.current, shadowRef.current], { clearProps: "opacity,visibility,transform" });
            setIsEntranceComplete(true);
          }
        });
      }
    });

    return () => st.kill();
  }, []);

  // Parallax Animation (GSAP quickTo)
  useEffect(() => {
    const gsap = window.gsap;
    if (!gsap || isMobile) return;

    const xTo = gsap.quickTo(parallaxRef.current, "x", { duration: 0.8, ease: "power3" });
    const yTo = gsap.quickTo(parallaxRef.current, "y", { duration: 0.8, ease: "power3" });
    const rotTo = gsap.quickTo(parallaxRef.current, "rotation", { duration: 0.8, ease: "power3" });

    const handleMouseMove = (e) => {
      const xRatio = (e.clientX / window.innerWidth) * 2 - 1;
      const yRatio = (e.clientY / window.innerHeight) * 2 - 1;

      xTo(xRatio * 12);
      yTo(yRatio * 8);
      rotTo(xRatio * 2);
    };

    window.addEventListener("mousemove", handleMouseMove);
    return () => window.removeEventListener("mousemove", handleMouseMove);
  }, [isMobile]);

  // Framer Motion Idle Animations
  const orbControls = useAnimation();
  const shadowControls = useAnimation();

  useEffect(() => {
    if (isEntranceComplete) {
      orbControls.start({
        y: [0, -16, -6, -20, 0].map(val => isMobile ? val * 0.5 : val),
        backgroundPositionX: ["0%", "200%"],
        scale: [1, 1.015, 1.03, 1.018, 1],
        transition: {
          y: { duration: 14, ease: "easeInOut", repeat: Infinity, repeatType: "mirror" },
          scale: { duration: 14, ease: "easeInOut", repeat: Infinity, repeatType: "mirror" },
          backgroundPositionX: { duration: 20, ease: "linear", repeat: Infinity, repeatType: "loop" }
        }
      });

      // Shadow animation synced
      shadowControls.start({
        scale: [1, 0.85, 0.92, 0.8, 1],
        opacity: [1, 0.6, 0.8, 0.5, 1],
        filter: ["blur(8px)", "blur(12px)", "blur(10px)", "blur(14px)", "blur(8px)"],
        transition: {
          duration: 14,
          ease: "easeInOut",
          repeat: Infinity,
          repeatType: "mirror"
        }
      });
    }
  }, [isEntranceComplete, orbControls, shadowControls, isMobile]);

  return (
    <div ref={containerRef} style={{ display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', minHeight: '300px', position: 'relative' }}>
      
      {/* Parallax Wrapper */}
      <div ref={parallaxRef} style={{ position: 'relative', display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
        
        {/* The 3D Scene Root */}
        <motion.div
          ref={orbRef}
          animate={orbControls}
          style={{
            width: `${orbSize}px`,
            height: `${orbSize}px`,
            visibility: 'hidden',
            willChange: 'transform, opacity',
            perspective: '1000px',
            transformStyle: 'preserve-3d',
            position: 'relative'
            // No overflow: hidden, allowing the logo to orbit outside like a satellite
          }}
        >
          {/* Layer 1: Opaque Sphere Base (Z=0) */}
          <motion.div
            style={{
              position: 'absolute',
              top: 0,
              left: 0,
              width: '100%',
              height: '100%',
              borderRadius: '50%',
              backgroundColor: '#ffffff',
              backgroundImage: 'repeating-linear-gradient(90deg, rgba(0,0,0,0) 0%, rgba(0,0,0,0.02) 20%, rgba(0,0,0,0) 40%)',
              backgroundSize: '200% 100%',
              transform: 'translateZ(0px)', 
              willChange: 'background-position',
              zIndex: 1
            }}
            animate={orbControls} 
          />

          {/* Layer 2: Spherical Lighting Overlay */}
          <div
            style={{
              position: 'absolute',
              top: 0,
              left: 0,
              width: '100%',
              height: '100%',
              borderRadius: '50%',
              boxShadow: 'inset -20px -20px 40px rgba(0,0,0,0.08), inset 10px 10px 20px rgba(255,255,255,0.9), inset 0 0 10px rgba(0,0,0,0.02)',
              transform: 'translateZ(1px)', 
              pointerEvents: 'none',
              zIndex: 2 // Renders strictly behind the floating logo satellite
            }}
          />

          {/* Layer 3: Logo and Cards Satellite Wrapper */}
          <motion.div
            style={{
              position: 'absolute',
              top: 0,
              left: 0,
              width: '100%',
              height: '100%',
              transformStyle: 'preserve-3d',
              display: 'flex',
              justifyContent: 'center',
              alignItems: 'center',
              zIndex: 3 // Renders ON TOP of the sphere's lighting
            }}
            animate={{ rotateY: [0, -360] }}
            transition={{ duration: 12, ease: "linear", repeat: Infinity }} // Slightly slower to read cards
          >
            {[
              { type: 'logo', angle: 0 },
              { type: 'card', name: 'Dinesh Kumar M', role: 'Founder & CEO', angle: 90, imgSrc: './assets/img/team/dinesh.png' },
              { type: 'card', name: 'Vardhan T', role: 'Full stack developer', angle: 180, imgSrc: './assets/img/team/vardhan.png' },
              { type: 'card', name: 'Abhiram B', role: 'Frontend developer', angle: 270 }
            ].map((item, idx) => (
              <div
                key={idx}
                style={{
                  position: 'absolute',
                  width: item.type === 'logo' ? '260px' : '180px',
                  height: item.type === 'logo' ? '130px' : '260px', // Vertical card height
                  transform: `rotateY(${item.angle}deg) translateZ(${orbSize / 2 + 50}px)`, 
                  backfaceVisibility: 'hidden',
                  WebkitBackfaceVisibility: 'hidden',
                  display: 'flex',
                  justifyContent: 'center',
                  alignItems: 'center',
                  ...(item.type === 'card' ? {
                    backgroundColor: '#ffffff',
                    borderRadius: '16px',
                    boxShadow: '0 10px 30px rgba(0,0,0,0.15), inset 0 0 0 1px rgba(255,255,255,0.6)',
                    overflow: 'hidden', // Clips the image to rounded corners
                    flexDirection: 'column'
                  } : {})
                }}
              >
                {item.type === 'logo' ? (
                  <img 
                    src="./assets/img/logo/logo.png" 
                    alt="Dexze" 
                    style={{ 
                      maxWidth: '100%', 
                      maxHeight: '100%', 
                      objectFit: 'contain',
                      filter: 'drop-shadow(10px 15px 15px rgba(0,0,0,0.3))'
                    }} 
                  />
                ) : (
                  <div style={{ width: '100%', height: '100%', display: 'flex', flexDirection: 'column' }}>
                    {/* Top 75%: Photo */}
                    <div style={{ 
                      height: '75%', 
                      width: '100%', 
                      backgroundColor: '#f4f4f4', 
                      display: 'flex', 
                      justifyContent: 'center', 
                      alignItems: 'center',
                      backgroundImage: item.imgSrc ? `url("${item.imgSrc}")` : 'url("https://via.placeholder.com/180x195/e0e0e0/999999?text=Photo")',
                      backgroundSize: 'cover',
                      backgroundPosition: 'center'
                    }} />
                    
                    {/* Bottom 25%: White Details Section */}
                    <div style={{ 
                      height: '25%', 
                      width: '100%', 
                      backgroundColor: '#ffffff', 
                      display: 'flex', 
                      flexDirection: 'column', 
                      justifyContent: 'center', 
                      alignItems: 'center',
                      borderTop: '1px solid #eaeaea',
                      padding: '0 10px',
                      textAlign: 'center'
                    }}>
                      <div style={{ fontWeight: '800', fontSize: '15px', color: '#111', lineHeight: '1.2' }}>{item.name}</div>
                      <div style={{ fontWeight: '600', fontSize: '11px', color: '#666', marginTop: '2px', textTransform: 'uppercase', letterSpacing: '0.5px' }}>{item.role}</div>
                    </div>
                  </div>
                )}
              </div>
            ))}
          </motion.div>
        </motion.div>

        {/* The Synchronized Shadow */}
        <motion.div
          ref={shadowRef}
          animate={shadowControls}
          style={{
            marginTop: '30px',
            width: `${orbSize * 0.75}px`,
            height: '14px',
            borderRadius: '50%',
            background: 'rgba(0, 0, 0, 0.12)',
            filter: 'blur(8px)',
            visibility: 'hidden', // Hidden until GSAP takes over
            willChange: 'transform, opacity, filter'
          }}
        />
        
      </div>
    </div>
  );
};

const rootNode = document.getElementById('orb-root');
if (rootNode) {
  const root = createRoot(rootNode);
  root.render(<PremiumOrb />);
}
