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

  // Start spin immediately so it syncs with logo and doesn't wait for scroll trigger
  useEffect(() => {
    orbControls.start({
      backgroundPositionX: ["0%", "200%"],
      transition: { duration: 9, ease: "linear", repeat: Infinity, repeatType: "loop" }
    });
  }, [orbControls]);

  useEffect(() => {
    if (isEntranceComplete) {
      // Start floating only after GSAP finishes entrance
      orbControls.start({
        y: [0, -16, -6, -20, 0].map(val => isMobile ? val * 0.5 : val),
        scale: [1, 1.015, 1.03, 1.018, 1],
        transition: {
          y: { duration: 14, ease: "easeInOut", repeat: Infinity, repeatType: "mirror" },
          scale: { duration: 14, ease: "easeInOut", repeat: Infinity, repeatType: "mirror" }
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
          {/* SINGLE SOLID CRYSTAL OBJECT */}
          <motion.div
            style={{
              position: 'absolute',
              top: 0,
              left: 0,
              width: '100%',
              height: '100%',
              borderRadius: '50%',
              backgroundColor: '#e2e8f0', // Deep crystal base
              backgroundImage: `url("data:image/svg+xml;charset=UTF-8,${encodeURIComponent(
                (() => {
                  let svg = '<svg xmlns="http://www.w3.org/2000/svg" width="800" height="415.692" viewBox="0 0 800 415.692"><defs><linearGradient id="c1" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#ffffff"/><stop offset="100%" stop-color="#e2e8f0"/></linearGradient><linearGradient id="c2" x1="20%" y1="0%" x2="80%" y2="100%"><stop offset="0%" stop-color="#f1f5f9"/><stop offset="48%" stop-color="#cbd5e1"/><stop offset="50%" stop-color="#ffffff"/><stop offset="52%" stop-color="#94a3b8"/><stop offset="100%" stop-color="#e2e8f0"/></linearGradient><linearGradient id="c3" x1="0%" y1="100%" x2="100%" y2="0%"><stop offset="0%" stop-color="#94a3b8"/><stop offset="40%" stop-color="#cbd5e1"/><stop offset="100%" stop-color="#f8fafc"/></linearGradient><linearGradient id="c4" x1="50%" y1="0%" x2="50%" y2="100%"><stop offset="0%" stop-color="#ffffff"/><stop offset="40%" stop-color="#f8fafc"/><stop offset="100%" stop-color="#cbd5e1"/></linearGradient><linearGradient id="c5" x1="100%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="#f8fafc"/><stop offset="40%" stop-color="#e2e8f0"/><stop offset="45%" stop-color="#ffffff"/><stop offset="55%" stop-color="#94a3b8"/><stop offset="100%" stop-color="#cbd5e1"/></linearGradient><linearGradient id="c6" x1="0%" y1="50%" x2="100%" y2="50%"><stop offset="0%" stop-color="#f1f5f9"/><stop offset="50%" stop-color="#cbd5e1"/><stop offset="100%" stop-color="#e2e8f0"/></linearGradient></defs><g stroke="rgba(0,0,0,0.06)" stroke-width="1.5" stroke-linejoin="bevel">';
                  const h = 69.282;
                  for (let r = 0; r < 6; r++) {
                    for (let c = -1; c < 11; c++) {
                      const x = c * 80 + (r % 2 === 1 ? 40 : 0);
                      const y = r * h;
                      const cWrap = (c + 10) % 10;
                      const fillUp = (r * 5 + cWrap * 7) % 6 + 1;
                      const fillDn = (r * 11 + cWrap * 13 + 3) % 6 + 1;
                      svg += '<polygon points="' + x + ',' + y + ' ' + (x+80) + ',' + y + ' ' + (x+40) + ',' + (y+h) + '" fill="url(#c' + fillUp + ')"/>';
                      svg += '<polygon points="' + (x+40) + ',' + (y+h) + ' ' + (x+120) + ',' + (y+h) + ' ' + (x+80) + ',' + y + '" fill="url(#c' + fillDn + ')"/>';
                    }
                  }
                  return svg + '</g></svg>';
                })()
              )}")`,
              backgroundSize: '200% auto',
              // Native physical volume bonded directly inside the single element
              boxShadow: `
                inset 15px 15px 40px rgba(255, 255, 255, 0.9),
                inset -20px -20px 40px rgba(0, 0, 0, 0.15),
                inset 0 0 20px rgba(0, 0, 0, 0.05)
              `,
              transform: 'translateZ(0px)',
              willChange: 'background-position',
              zIndex: 1
            }}
            animate={orbControls}
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
            transition={{ duration: 9, ease: "linear", repeat: Infinity }}
          >
            {[
              { type: 'logo', angle: 0 },
              { type: 'text', text: "BUILT FOR WHAT'S NEXT!", angle: 180 }
              /*
              // People cards hidden for now, kept for future use:
              { type: 'card', name: 'Dinesh Kumar M', role: 'Founder & CEO', angle: 90, imgSrc: './assets/img/team/dinesh.png' },
              { type: 'card', name: 'Vardhan T', role: 'Full stack developer', angle: 180, imgSrc: './assets/img/team/vardhan.png' },
              { type: 'card', name: 'Abhiram B', role: 'Frontend developer', angle: 270 }
              */
            ].map((item, idx) => {
              if (item.type === 'card') return null; // Safe guard if uncommented improperly

              const isLogo = item.type === 'logo';

              return (
                <motion.div
                  key={idx}
                  style={{
                    position: 'absolute',
                    width: item.type === 'logo' ? (isMobile ? '180px' : '260px') : item.type === 'text' ? (isMobile ? '240px' : '320px') : '20px',
                    height: item.type === 'logo' ? (isMobile ? '90px' : '130px') : item.type === 'card' ? '260px' : '50px',
                    transform: `rotateY(${item.angle}deg) translateZ(${orbSize / 2 + (isMobile ? 30 : 50)}px)`,
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
                  ) : item.type === 'text' ? (
                    <div style={{
                      fontWeight: '900',
                      fontSize: isMobile ? '24px' : '34px',
                      color: '#000000',
                      letterSpacing: '-1.5px',
                      textTransform: 'uppercase',
                      textAlign: 'center',
                      whiteSpace: 'nowrap',
                      fontFamily: 'var(--td-ff-heading, inherit)'
                    }}>
                      {item.text}
                    </div>
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
                </motion.div>
              )
            })}
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
            background: 'rgba(0, 0, 0, 0.25)',
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
