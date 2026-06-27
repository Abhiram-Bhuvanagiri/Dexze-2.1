import re

html_code = """
                    <!-- Interactive Ideas Section -->
                    <div class="interactive-ideas-container" style="max-width: 1400px; width: 100%; margin: 80px auto; padding: 0 32px; display: flex; gap: 80px; align-items: flex-start; position: relative;">
                        
                        <!-- Left Side: Editorial List (40%) -->
                        <div class="ideas-list-panel" style="width: 35%; display: flex; flex-direction: column; gap: 0;">
                            
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
                        <div class="ideas-display-panel" style="width: 65%; position: sticky; top: 120px; display: flex; flex-direction: column; gap: 40px;">
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
                        }

                        /* Left Side List */
                        .idea-list-item {
                            padding: 32px 0;
                            border-bottom: 1px solid rgba(0,0,0,0.1);
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
                            color: #999;
                            transition: color 0.4s ease;
                        }
                        .idea-list-item.active .idea-number {
                            color: var(--td-color-theme, #6a35ff);
                        }
                        
                        .idea-heading {
                            font-family: var(--td-ff-heading), sans-serif;
                            font-size: clamp(24px, 2.5vw, 36px);
                            font-weight: 500;
                            color: #666;
                            margin: 0;
                            transition: all 0.4s ease;
                            text-transform: capitalize;
                            letter-spacing: -0.5px;
                        }
                        .idea-list-item.active .idea-heading {
                            font-weight: 700;
                            color: #111;
                            transform: translateX(6px);
                        }

                        /* Right Side Image */
                        .ideas-images-wrapper {
                            width: 100%;
                            aspect-ratio: 16/10;
                            position: relative;
                            border-radius: 16px;
                            overflow: hidden;
                            box-shadow: 0 16px 40px rgba(0,0,0,0.06);
                            background: #f4f6f8;
                            transition: transform 0.4s ease, box-shadow 0.4s ease;
                            cursor: default;
                        }
                        .ideas-images-wrapper:hover {
                            transform: translateY(-4px);
                            box-shadow: 0 24px 60px rgba(0,0,0,0.12);
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
                            position: relative;
                            min-height: 250px;
                        }
                        .idea-text-content {
                            position: absolute;
                            top: 0;
                            left: 0;
                            width: 100%;
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
                            color: #111;
                            line-height: 1.15;
                            margin-bottom: 16px;
                            letter-spacing: -1px;
                            text-transform: uppercase;
                            opacity: 0;
                            transform: translateY(20px);
                            transition: opacity 0.5s ease, transform 0.5s ease;
                        }
                        .idea-text-content p {
                            color: #666;
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
                            flex-direction: column;
                            gap: 12px;
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
                            color: #333;
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
                                gap: 48px;
                            }
                            .ideas-list-panel {
                                width: 100% !important;
                            }
                            .ideas-display-panel {
                                width: 100% !important;
                                position: static !important;
                            }
                            .idea-list-item {
                                padding: 20px 0;
                            }
                            .idea-heading {
                                font-size: 28px;
                            }
                        }
                    </style>

                    <script>
                        document.addEventListener('DOMContentLoaded', () => {
                            const listItems = document.querySelectorAll('.idea-list-item');
                            const images = document.querySelectorAll('.idea-image');
                            const texts = document.querySelectorAll('.idea-text-content');
                            const imgWrapper = document.querySelector('.ideas-images-wrapper');
                            
                            function setActiveStage(index) {
                                listItems.forEach(item => item.classList.remove('active'));
                                images.forEach(img => img.classList.remove('active'));
                                texts.forEach(txt => txt.classList.remove('active'));
                                
                                listItems[index].classList.add('active');
                                images[index].classList.add('active');
                                texts[index].classList.add('active');
                            }
                            
                            listItems.forEach((item, index) => {
                                // Desktop Hover
                                item.addEventListener('mouseenter', () => {
                                    if (window.innerWidth > 991) {
                                        setActiveStage(index);
                                    }
                                });
                                // Mobile Tap
                                item.addEventListener('click', () => {
                                    if (window.innerWidth <= 991) {
                                        setActiveStage(index);
                                    }
                                });
                            });

                            // Gentle Parallax
                            if (imgWrapper) {
                                imgWrapper.addEventListener('mousemove', (e) => {
                                    const rect = imgWrapper.getBoundingClientRect();
                                    const x = e.clientX - rect.left - rect.width / 2;
                                    const y = e.clientY - rect.top - rect.height / 2;
                                    
                                    const moveX = (x / rect.width) * 10;
                                    const moveY = (y / rect.height) * 10;
                                    
                                    const activeImg = imgWrapper.querySelector('.idea-image.active');
                                    if (activeImg) {
                                        activeImg.style.transition = 'none';
                                        activeImg.style.transform = `scale(1.02) translate(${moveX}px, ${moveY}px)`;
                                    }
                                });
                                
                                imgWrapper.addEventListener('mouseleave', () => {
                                    const activeImg = imgWrapper.querySelector('.idea-image.active');
                                    if (activeImg) {
                                        activeImg.style.transition = 'opacity 0.6s cubic-bezier(0.4, 0, 0.2, 1), transform 0.6s cubic-bezier(0.4, 0, 0.2, 1)';
                                        activeImg.style.transform = 'scale(1) translate(0, 0)';
                                    }
                                });
                            }
                        });
                    </script>
"""

with open('services-2.html', 'r', encoding='utf-8') as f:
    original = f.read()

# Using regex to find the block to replace.
# Starts from: <!-- Ideas Become Products Section -->
# Ends before: <!-- Technology Marquee Section -->
pattern = re.compile(r'<!-- Ideas Become Products Section -->.*?(?=<!-- Technology Marquee Section -->)', re.DOTALL)

# Ensure match is found
if pattern.search(original):
    new_content = pattern.sub(html_code + '\n                ', original)
    with open('services-2.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully replaced GSAP section with Interactive Hover layout.")
else:
    print("Could not find the target section to replace.")
