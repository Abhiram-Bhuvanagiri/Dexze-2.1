import re

with open('services-2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Core Expertise Section
# Change section background
content = content.replace(
    '<section id="tech-scroll-section" style="background-color: #161616; padding: 100px 0 50px 0; position: relative;">',
    '<section id="tech-scroll-section" style="background-color: #f7f9fa; padding: 100px 0 50px 0; position: relative;">'
)

# Change subtitle color
content = content.replace(
    '<span style="font-family: var(--td-ff-body), sans-serif; font-size: 13px; font-weight: 600; color: #aaa; text-transform: uppercase; letter-spacing: 2px;">Core Expertise</span>',
    '<span style="font-family: var(--td-ff-body), sans-serif; font-size: 13px; font-weight: 600; color: #111; text-transform: uppercase; letter-spacing: 2px;">Core Expertise</span>'
)
content = content.replace(
    '<div style="height: 1px; width: 40px; background-color: #444;"></div>\n                            <span style="font-family: var(--td-ff-body), sans-serif; font-size: 13px; font-weight: 600; color: #111; text-transform: uppercase; letter-spacing: 2px;">Core Expertise</span>\n                            <div style="height: 1px; width: 40px; background-color: #444;"></div>',
    '<div style="height: 1px; width: 40px; background-color: #d2d2d2;"></div>\n                            <span style="font-family: var(--td-ff-body), sans-serif; font-size: 13px; font-weight: 600; color: #111; text-transform: uppercase; letter-spacing: 2px;">Core Expertise</span>\n                            <div style="height: 1px; width: 40px; background-color: #d2d2d2;"></div>'
)

# Change heading color
content = content.replace(
    '<h2 style="font-family: var(--td-ff-heading), sans-serif; font-size: clamp(40px, 6vw, 80px); font-weight: 800; color: #ffffff; line-height: 1.05; margin-bottom: 32px; letter-spacing: -2px;">\n                            Engineering the future<br>of your business\n                        </h2>',
    '<h2 style="font-family: var(--td-ff-heading), sans-serif; font-size: clamp(40px, 6vw, 80px); font-weight: 800; color: #000; line-height: 1.05; margin-bottom: 32px; letter-spacing: -2px;">\n                            Engineering the future<br>of your business\n                        </h2>'
)

# Change paragraph color
content = content.replace(
    '<p style="font-family: var(--td-ff-body), sans-serif; font-size: 20px; font-weight: 400; color: #999999; max-width: 700px; margin: 0 auto; line-height: 1.8;">\n                            From immersive mobile experiences to autonomous AI systems, we deliver end-to-end technological excellence.\n                        </p>',
    '<p style="font-family: var(--td-ff-body), sans-serif; font-size: 20px; font-weight: 400; color: #666; max-width: 700px; margin: 0 auto; line-height: 1.8;">\n                            From immersive mobile experiences to autonomous AI systems, we deliver end-to-end technological excellence.\n                        </p>'
)

# Ideas Become Products Section
# Change section background
content = content.replace(
    '<section id="ideas-become-products-section" style="background-color: #161616; position: relative; width: 100%; overflow: visible; z-index: 10;">',
    '<section id="ideas-become-products-section" style="background-color: #ffffff; position: relative; width: 100%; overflow: visible; z-index: 10;">'
)

# Change subtitle color
content = content.replace(
    '<span style="font-family: var(--td-ff-body), sans-serif; font-size: 13px; font-weight: 600; color: #aaa; text-transform: uppercase; letter-spacing: 2px;">FROM AN IDEA TO A PRODUCT</span>',
    '<span style="font-family: var(--td-ff-body), sans-serif; font-size: 13px; font-weight: 600; color: #111; text-transform: uppercase; letter-spacing: 2px;">FROM AN IDEA TO A PRODUCT</span>'
)
content = content.replace(
    '<div style="height: 1px; width: 40px; background-color: #444;"></div>\n                            <span style="font-family: var(--td-ff-body), sans-serif; font-size: 13px; font-weight: 600; color: #111; text-transform: uppercase; letter-spacing: 2px;">FROM AN IDEA TO A PRODUCT</span>\n                            <div style="height: 1px; width: 40px; background-color: #444;"></div>',
    '<div style="height: 1px; width: 40px; background-color: #d2d2d2;"></div>\n                            <span style="font-family: var(--td-ff-body), sans-serif; font-size: 13px; font-weight: 600; color: #111; text-transform: uppercase; letter-spacing: 2px;">FROM AN IDEA TO A PRODUCT</span>\n                            <div style="height: 1px; width: 40px; background-color: #d2d2d2;"></div>'
)

# Change heading color
content = content.replace(
    '<h2 style="font-family: var(--td-ff-heading), sans-serif; font-size: clamp(40px, 6vw, 80px); font-weight: 800; color: #ffffff; line-height: 1.05; margin-bottom: 32px; letter-spacing: -2px;">\n                            Bring your ideas to life.\n                        </h2>',
    '<h2 style="font-family: var(--td-ff-heading), sans-serif; font-size: clamp(40px, 6vw, 80px); font-weight: 800; color: #000; line-height: 1.05; margin-bottom: 32px; letter-spacing: -2px;">\n                            Bring your ideas to life.\n                        </h2>'
)

# Change paragraph color
content = content.replace(
    '<p style="font-family: var(--td-ff-body), sans-serif; font-size: 20px; font-weight: 400; color: #999999; max-width: 700px; margin: 0 auto; line-height: 1.8;">\n                            We guide you through every stage of the product lifecycle—from initial discovery and design to development, testing, and scalable deployment. Partner with us to build digital experiences that matter.\n                        </p>',
    '<p style="font-family: var(--td-ff-body), sans-serif; font-size: 20px; font-weight: 400; color: #666; max-width: 700px; margin: 0 auto; line-height: 1.8;">\n                            We guide you through every stage of the product lifecycle—from initial discovery and design to development, testing, and scalable deployment. Partner with us to build digital experiences that matter.\n                        </p>'
)

with open('services-2.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated heading backgrounds and text colors!")
