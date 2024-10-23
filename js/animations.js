// Initialize GSAP Animations
gsap.registerPlugin(ScrollMagic);

// Fade In Elements
gsap.utils.toArray('.fade-in').forEach((elem) => {
    gsap.from(elem, {
        duration: 1,
        opacity: 0,
        y: 50,
        ease: "power1.out",
        scrollTrigger: {
            trigger: elem,
            start: "top 80%",
            toggleActions: "play none none none"
        }
    });
});

// Slide In Left
gsap.utils.toArray('.slide-in-left').forEach((elem) => {
    gsap.from(elem, {
        duration: 1,
        x: -100,
        opacity: 0,
        ease: "power1.out",
        scrollTrigger: {
            trigger: elem,
            start: "top 80%",
            toggleActions: "play none none none"
        }
    });
});

// Slide In Right
gsap.utils.toArray('.slide-in-right').forEach((elem) => {
    gsap.from(elem, {
        duration: 1,
        x: 100,
        opacity: 0,
        ease: "power1.out",
        scrollTrigger: {
            trigger: elem,
            start: "top 80%",
            toggleActions: "play none none none"
        }
    });
});
