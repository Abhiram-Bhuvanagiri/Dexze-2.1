import re

def apply_all_fixes():
    with open('services-2.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Core Expertise typography and full-bleed image
    # Subtitle pill -> Line subtitle
    content = content.replace(
        '<span style="background-color: rgba(106, 53, 255, 0.1); color: var(--td-color-theme, #6a35ff); padding: 6px 16px; border-radius: 40px; font-size: 13px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px;">Core Expertise</span>',
        '<div style="display: flex; align-items: center; gap: 16px; margin-bottom: 24px;">\n                            <div style="height: 1px; width: 40px; background-color: #d2d2d2;"></div>\n                            <span style="font-family: var(--td-ff-body), sans-serif; font-size: 13px; font-weight: 600; color: #111; text-transform: uppercase; letter-spacing: 2px;">Core Expertise</span>\n                            <div style="height: 1px; width: 40px; background-color: #d2d2d2;"></div>\n                        </div>'
    )
    
    # Heading style
    content = content.replace(
        '<h2 style="font-size: clamp(32px, 5vw, 56px); font-weight: 700; color: #111; line-height: 1.1; margin-bottom: 24px; letter-spacing: -1px;">\n                            Engineering the future<br>of your business\n                        </h2>',
        '<h2 style="font-family: var(--td-ff-heading), sans-serif; font-size: clamp(40px, 6vw, 80px); font-weight: 800; color: #000; line-height: 1.05; margin-bottom: 32px; letter-spacing: -2px;">\n                            Engineering the future<br>of your business\n                        </h2>'
    )
    
    # Paragraph style
    content = content.replace(
        '<p style="font-size: 18px; color: #666; max-width: 700px; margin: 0 auto; line-height: 1.6;">\n                            From immersive mobile experiences to autonomous AI systems, we deliver end-to-end technological excellence.\n                        </p>',
        '<p style="font-family: var(--td-ff-body), sans-serif; font-size: 20px; font-weight: 400; color: #666; max-width: 700px; margin: 0 auto; line-height: 1.8;">\n                            From immersive mobile experiences to autonomous AI systems, we deliver end-to-end technological excellence.\n                        </p>'
    )

    # Make Unveil Cards Dark Mode and Full Bleed
    content = re.sub(
        r'<div class="unveil-card-inner" style="background: #fff;',
        r'<div class="unveil-card-inner" style="background: #1a1a1a;',
        content
    )
    # Change dark text to white for Dark Mode cards
    content = re.sub(
        r'<h3 style="font-size: 32px; font-weight: 700; color: #111; margin-bottom: 16px;">',
        r'<h3 style="font-size: 32px; font-weight: 700; color: #fff; margin-bottom: 16px;">',
        content
    )
    
    content = re.sub(
        r'class="unveil-card-right" style="width: 50%; background: #222; display: flex; align-items: center; justify-content: center; position: relative; padding: 24px;">\s*<img src="([^"]+)" style="width: 100%; height: 100%; object-fit: cover; border-radius: 16px; box-shadow: 0 16px 40px rgba\(0,0,0,0\.1\);" class="unveil-img">',
        r'class="unveil-card-right" style="width: 50%; background: #222; display: flex; align-items: center; justify-content: center; position: relative; padding: 0;">\n                                            <img src="\1" style="width: 100%; height: 100%; object-fit: cover; border-radius: 0; box-shadow: none;" class="unveil-img">',
        content, flags=re.DOTALL
    )

    # 2. Update Scale with Dexze typography
    content = content.replace(
        '<span style="background-color: rgba(106, 53, 255, 0.1); color: var(--td-color-theme, #6a35ff); padding: 6px 16px; border-radius: 40px; font-size: 13px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; display: inline-block; margin-bottom: 16px;">Scale with Dexze</span>',
        '<div style="display: flex; align-items: center; gap: 16px; margin-bottom: 24px;">\n                            <div style="height: 1px; width: 40px; background-color: #d2d2d2;"></div>\n                            <span style="font-family: var(--td-ff-body), sans-serif; font-size: 13px; font-weight: 600; color: #111; text-transform: uppercase; letter-spacing: 2px;">Scale with Dexze</span>\n                        </div>'
    )
    content = content.replace(
        '<h2 style="font-size: clamp(32px, 4vw, 48px); font-weight: 700; color: #111; line-height: 1.1; margin-bottom: 24px; letter-spacing: -1px;">\n                                Building the foundation for exponential growth.\n                            </h2>',
        '<h2 style="font-family: var(--td-ff-heading), sans-serif; font-size: clamp(40px, 5vw, 64px); font-weight: 800; color: #000; line-height: 1.05; margin-bottom: 32px; letter-spacing: -2px;">\n                                Building the foundation for exponential growth.\n                            </h2>'
    )
    content = content.replace(
        '<p style="font-size: 16px; color: #666; line-height: 1.6; margin-bottom: 32px;">\n                                We don\'t just write code; we build scalable digital architectures designed to handle millions of users effortlessly. Our cloud-native approach ensures your product remains fast, secure, and reliable, no matter how much you scale.\n                            </p>',
        '<p style="font-family: var(--td-ff-body), sans-serif; font-size: 20px; font-weight: 400; color: #666; line-height: 1.8; margin-bottom: 32px;">\n                                We don\'t just write code; we build scalable digital architectures designed to handle millions of users effortlessly. Our cloud-native approach ensures your product remains fast, secure, and reliable, no matter how much you scale.\n                            </p>'
    )

    # 3. Update Ideas Become Products to New Hover Layout
    # First update the heading portion to match the typography
    content = content.replace(
        '<span style="background-color: rgba(106, 53, 255, 0.1); color: var(--td-color-theme, #6a35ff); padding: 6px 16px; border-radius: 40px; font-size: 13px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px;">From an idea to a product</span>',
        '<div style="display: flex; align-items: center; justify-content: center; gap: 16px; margin-bottom: 24px;">\n                            <div style="height: 1px; width: 40px; background-color: #d2d2d2;"></div>\n                            <span style="font-family: var(--td-ff-body), sans-serif; font-size: 13px; font-weight: 600; color: #111; text-transform: uppercase; letter-spacing: 2px;">FROM AN IDEA TO A PRODUCT</span>\n                            <div style="height: 1px; width: 40px; background-color: #d2d2d2;"></div>\n                        </div>'
    )
    content = content.replace(
        '<h2 style="font-size: clamp(32px, 5vw, 56px); font-weight: 700; color: #111; line-height: 1.1; margin-bottom: 24px; letter-spacing: -1px;">\n                            Bring your ideas to life.\n                        </h2>',
        '<h2 style="font-family: var(--td-ff-heading), sans-serif; font-size: clamp(40px, 6vw, 80px); font-weight: 800; color: #000; line-height: 1.05; margin-bottom: 32px; letter-spacing: -2px;">\n                            Bring your ideas to life.\n                        </h2>'
    )
    content = content.replace(
        '<p style="font-size: 18px; color: #666; max-width: 700px; margin: 0 auto; line-height: 1.6;">\n                            We guide you through every stage of the product lifecycle—from initial discovery and design to development, testing, and scalable deployment.\n                        </p>',
        '<p style="font-family: var(--td-ff-body), sans-serif; font-size: 20px; font-weight: 400; color: #666; max-width: 700px; margin: 0 auto; line-height: 1.8;">\n                            We guide you through every stage of the product lifecycle—from initial discovery and design to development, testing, and scalable deployment. Partner with us to build digital experiences that matter.\n                        </p>'
    )

    # 4. Tech Marquee Heading update
    content = content.replace(
        '<h3 style="font-size: clamp(28px, 4vw, 42px); font-weight: 700; color: #111; margin-bottom: 16px; letter-spacing: -1px;">Technologies we master</h3>',
        '<h3 style="font-family: var(--td-ff-heading), sans-serif; font-size: clamp(40px, 6vw, 80px); font-weight: 800; color: #000; line-height: 1.05; margin-bottom: 32px; letter-spacing: -2px;">Technologies we master</h3>'
    )

    html_code = """
                    <!-- Interactive Ideas Section -->
                    <div class="interactive-ideas-container" style="max-width: 1400px; width: 100%; margin: 80px auto; padding: 0 32px; display: flex; gap: 80px; align-items: flex-start; position: relative; background: #1a1a1a; border-radius: 24px;">
                        
                        <!-- Left Side: Editorial List (40%) -->
                        <div class="ideas-list-panel" style="width: 35%; display: flex; flex-direction: column; gap: 0; padding: 40px;">
                            
                            <!-- Item 1 -->
                            <div class="idea-list-item active" data-index="0">
                                <div class="idea-list-active-line"></div>
                                <span class="idea-number">01</span>
                                <h3 class="idea-heading">Discovery</h3>
                            </div>
                            
                            <!-- Item 2 -->
                            <div class="idea-list-item" data-index="1">
                                <div class="idea-list-active-line"></div>
                                <span class="idea-number">02</span>
                                <h3 class="idea-heading">Wireframes</h3>
                            </div>

                            <!-- Item 3 -->
                            <div class="idea-list-item" data-index="2">
                                <div class="idea-list-active-line"></div>
                                <span class="idea-number">03</span>
                                <h3 class="idea-heading">UI Design</h3>
                            </div>

                            <!-- Item 4 -->
                            <div class="idea-list-item" data-index="3">
                                <div class="idea-list-active-line"></div>
                                <span class="idea-number">04</span>
                                <h3 class="idea-heading">Development</h3>
                            </div>

                            <!-- Item 5 -->
                            <div class="idea-list-item" data-index="4">
                                <div class="idea-list-active-line"></div>
                                <span class="idea-number">05</span>
                                <h3 class="idea-heading">Testing</h3>
                            </div>

                            <!-- Item 6 -->
                            <div class="idea-list-item" data-index="5">
                                <div class="idea-list-active-line"></div>
                                <span class="idea-number">06</span>
                                <h3 class="idea-heading">Launch</h3>
                            </div>

                        </div>

                        <!-- Right Side: Visual & Text (65%) -->
                        <div class="ideas-display-panel" style="width: 65%; position: sticky; top: 120px; display: flex; flex-direction: column; gap: 0;">
                            <!-- Images Wrapper -->
                            <div class="ideas-images-wrapper">
                                <img class="idea-image active" src="assets/img/services-2/discovery.png" alt="Discovery">
                                <img class="idea-image" src="assets/img/services-2/wireframes.png" alt="Wireframes">
                                <img class="idea-image" src="assets/img/services-2/ui-design.png" alt="UI Design">
                                <img class="idea-image" src="assets/img/services-2/development.png" alt="Development">
                                <img class="idea-image" src="assets/img/services-2/testing.png" alt="Testing">
                                <img class="idea-image" src="assets/img/services-2/launch.png" alt="Launch">
                            </div>

                            <!-- Text Wrapper -->
                            <div class="ideas-text-wrapper">
                                
                                <!-- Text 1 -->
                                <div class="idea-text-content active">
                                    <h3>Discovery</h3>
                                    <p>Understanding the business, users, pain points and goals. We lay a solid foundation for the entire product lifecycle.</p>
                                    <ul>
                                        <li><span></span> Strategy workshop</li>
                                        <li><span></span> Business planning</li>
                                        <li><span></span> Product discussion</li>
                                    </ul>
                                </div>

                                <!-- Text 2 -->
                                <div class="idea-text-content">
                                    <h3>Wireframes</h3>
                                    <p>Mapping out user journeys and structural layouts. This crucial step ensures logical flow and intuitive navigation.</p>
                                    <ul>
                                        <li><span></span> UX sketches</li>
                                        <li><span></span> Low-fidelity layouts</li>
                                        <li><span></span> User flows</li>
                                    </ul>
                                </div>

                                <!-- Text 3 -->
                                <div class="idea-text-content">
                                    <h3>UI Design</h3>
                                    <p>Creating premium, high-fidelity visual interfaces and style guides that captivate your target audience.</p>
                                    <ul>
                                        <li><span></span> Figma screens</li>
                                        <li><span></span> Design systems</li>
                                        <li><span></span> Modern UI compositions</li>
                                    </ul>
                                </div>

                                <!-- Text 4 -->
                                <div class="idea-text-content">
                                    <h3>Development</h3>
                                    <p>Translating designs into clean, production-ready code with robust, scalable architectures.</p>
                                    <ul>
                                        <li><span></span> Enterprise SaaS dashboard</li>
                                        <li><span></span> Web application</li>
                                        <li><span></span> Mobile application</li>
                                    </ul>
                                </div>

                                <!-- Text 5 -->
                                <div class="idea-text-content">
                                    <h3>Testing</h3>
                                    <p>Rigorous quality assurance, automated integration testing, and manual checks to ensure bug-free operation.</p>
                                    <ul>
                                        <li><span></span> QA dashboard</li>
                                        <li><span></span> Analytics</li>
                                        <li><span></span> Bug tracking</li>
                                    </ul>
                                </div>

                                <!-- Text 6 -->
                                <div class="idea-text-content">
                                    <h3>Launch</h3>
                                    <p>Deploying the product smoothly to production servers with zero-downtime deployment strategies.</p>
                                    <ul>
                                        <li><span></span> Live product</li>
                                        <li><span></span> Business analytics</li>
                                        <li><span></span> User adoption</li>
                                    </ul>
                                </div>

                            </div>
                        </div>
                    </div>

                    <style>
                        /* Interactive Ideas CSS */
                        .interactive-ideas-container {
                            min-height: 80vh;
                            overflow: hidden;
                        }

                        /* Left Side List */
                        .idea-list-item {
                            padding: 32px 0;
                            border-bottom: 1px solid rgba(255,255,255,0.05);
                            cursor: pointer;
                            display: flex;
                            align-items: baseline;
                            gap: 24px;
                            position: relative;
                            transition: all 0.4s ease;
                        }
                        .idea-list-item:last-child {
                            border-bottom: none;
                        }
                        
                        .idea-list-active-line {
                            position: absolute;
                            left: -24px;
                            top: 50%;
                            transform: translateY(-50%);
                            width: 0;
                            height: 2px;
                            background: var(--td-color-theme, #6a35ff);
                            transition: width 0.4s ease;
                        }
                        .idea-list-item.active .idea-list-active-line {
                            width: 16px;
                        }
                        
                        .idea-number {
                            font-family: var(--td-ff-heading), sans-serif;
                            font-size: 24px;
                            font-weight: 500;
                            color: #666;
                            transition: color 0.4s ease;
                        }
                        .idea-list-item.active .idea-number {
                            color: var(--td-color-theme, #6a35ff);
                        }
                        
                        .idea-heading {
                            font-family: var(--td-ff-heading), sans-serif;
                            font-size: clamp(24px, 2.5vw, 36px);
                            font-weight: 500;
                            color: #999;
                            margin: 0;
                            transition: all 0.4s ease;
                            text-transform: capitalize;
                            letter-spacing: -0.5px;
                        }
                        .idea-list-item.active .idea-heading {
                            font-weight: 700;
                            color: #fff;
                            transform: translateX(6px);
                        }

                        /* Right Side Image */
                        .ideas-images-wrapper {
                            width: 100%;
                            height: 100%;
                            position: absolute;
                            top: 0;
                            right: 0;
                            border-radius: 0;
                            overflow: hidden;
                            background: #222;
                            transition: transform 0.4s ease, box-shadow 0.4s ease;
                            cursor: default;
                        }
                        .idea-image {
                            position: absolute;
                            top: 0;
                            left: 0;
                            width: 100%;
                            height: 100%;
                            object-fit: cover;
                            opacity: 0;
                            transform: scale(1.03);
                            transition: opacity 0.6s cubic-bezier(0.4, 0, 0.2, 1), transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
                            will-change: transform, opacity;
                        }
                        .idea-image.active {
                            opacity: 1;
                            transform: scale(1);
                        }

                        /* Right Side Text */
                        .ideas-text-wrapper {
                            width: 100%;
                            position: absolute;
                            bottom: 0;
                            left: 0;
                            padding: 40px;
                            background: linear-gradient(to top, rgba(0,0,0,0.8), rgba(0,0,0,0));
                            z-index: 2;
                        }
                        .idea-text-content {
                            position: absolute;
                            bottom: 40px;
                            left: 40px;
                            width: calc(100% - 80px);
                            opacity: 0;
                            pointer-events: none;
                        }
                        .idea-text-content.active {
                            opacity: 1;
                            pointer-events: auto;
                        }
                        
                        .idea-text-content h3 {
                            font-family: var(--td-ff-heading), sans-serif;
                            font-size: clamp(28px, 3vw, 42px);
                            font-weight: 700;
                            color: #fff;
                            line-height: 1.15;
                            margin-bottom: 16px;
                            letter-spacing: -1px;
                            text-transform: uppercase;
                            opacity: 0;
                            transform: translateY(20px);
                            transition: opacity 0.5s ease, transform 0.5s ease;
                        }
                        .idea-text-content p {
                            color: #ccc;
                            font-size: 18px;
                            line-height: 1.6;
                            margin-bottom: 24px;
                            max-width: 90%;
                            opacity: 0;
                            transform: translateY(20px);
                            transition: opacity 0.5s ease 0.1s, transform 0.5s ease 0.1s;
                        }
                        .idea-text-content ul {
                            list-style: none;
                            padding: 0;
                            margin: 0;
                            display: flex;
                            flex-wrap: wrap;
                            gap: 16px;
                            opacity: 0;
                            transform: translateY(20px);
                            transition: opacity 0.5s ease 0.2s, transform 0.5s ease 0.2s;
                        }
                        .idea-text-content ul li {
                            display: flex;
                            align-items: center;
                            gap: 12px;
                            font-size: 16px;
                            font-weight: 500;
                            color: #ddd;
                        }
                        .idea-text-content ul li span {
                            display: inline-block;
                            width: 6px;
                            height: 6px;
                            background: var(--td-color-theme, #6a35ff);
                            border-radius: 50%;
                        }
                        
                        .idea-text-content.active h3,
                        .idea-text-content.active p,
                        .idea-text-content.active ul {
                            opacity: 1;
                            transform: translateY(0);
                        }

                        /* Responsive */
                        @media (max-width: 991.98px) {
                            .interactive-ideas-container {
                                flex-direction: column;
                                gap: 0;
                                padding: 0;
                            }
                            .ideas-list-panel {
                                width: 100% !important;
                                padding: 24px !important;
                            }
                            .ideas-display-panel {
                                width: 100% !important;
                                position: static !important;
                                height: 50vh !important;
                            }
                            .ideas-images-wrapper {
                                position: relative;
                            }
                            .idea-text-content {
                                left: 24px;
                                bottom: 24px;
                                width: calc(100% - 48px);
                            }
                        }
                    </style>

                    <script>
                        document.addEventListener('DOMContentLoaded', () => {
                            const listItems = document.querySelectorAll('.idea-list-item');
                            const images = document.querySelectorAll('.idea-image');
                            const texts = document.querySelectorAll('.idea-text-content');
                            
                            function setActiveStage(index) {
                                listItems.forEach(item => item.classList.remove('active'));
                                images.forEach(img => img.classList.remove('active'));
                                texts.forEach(txt => txt.classList.remove('active'));
                                
                                listItems[index].classList.add('active');
                                images[index].classList.add('active');
                                texts[index].classList.add('active');
                            }
                            
                            listItems.forEach((item, index) => {
                                item.addEventListener('mouseenter', () => {
                                    if (window.innerWidth > 991) {
                                        setActiveStage(index);
                                    }
                                });
                                item.addEventListener('click', () => {
                                    if (window.innerWidth <= 991) {
                                        setActiveStage(index);
                                    }
                                });
                            });
                        });
                    </script>
"""
    # Replace the scroll-storytelling area
    pattern = re.compile(r'<!-- Pinned storytelling area -->.*?(?=<!-- Technology Marquee Section -->)', re.DOTALL)
    content = pattern.sub(html_code + '\n                ', content)

    with open('services-2.html', 'w', encoding='utf-8') as f:
        f.write(content)
        
apply_all_fixes()
