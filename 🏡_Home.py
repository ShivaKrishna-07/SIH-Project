import streamlit as st
import streamlit.components.v1 as components  # Correct import for components


st.title("Home")

home_form = """
    <style>
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: #333;
            padding: 10px;
        }
        
        .navbar ul {
            list-style-type: none;
            display: flex;
            margin: 0;
            padding: 0;
        }
        
        .navbar ul li {
            margin: 0 15px;
        }
        
        .navbar ul li a, .navbar button a {
            color: white;
            text-decoration: none;
            font-weight: bold;
        }
        
        .navbar .logo a {
            color: white;
            font-size: 1.5em;
            text-decoration: none;
            font-weight: bold;
        }
        
        .navbar button {
            background-color: #4CAF50;
            border: none;
            padding: 10px 20px;
            margin-left: 10px;
            cursor: pointer;
            color: white;
        }
        
        .section1 {
            text-align: center;
            padding: 100px;
            background-color: #f4f4f4;
        }
        
        .section2 {
            padding: 50px;
            text-align: center;
            background-color: #e2e2e2;
        }
        
        .services {
            display: flex;
            justify-content: center;
            gap: 20px;
        }
        
        .services .service {
            background-color: #4CAF50;
            padding: 20px;
            border-radius: 10px;
            color: white;
            cursor: pointer;
        }
        
        .section3 {
            padding: 50px;
            background-color: #ddd;
            text-align: center;
        }
        
        footer {
            padding: 20px;
            background-color: #333;
            color: white;
            text-align: center;
        }
        
        .reveal {
            opacity: 0;
            transform: translateY(50px);
            transition: all 0.7s ease-in-out;
        }
        
        .reveal.active {
            opacity: 1;
            transform: translateY(0);
        }
    </style>

    <nav class="navbar">
        <div class="logo"><a href="#">Farmers Guide</a></div>
        <ul>
            <li><a href="#">Home</a></li>
            <li><a href="#">Services</a></li>
            <li><a href="#">Contact</a></li>
            <li><a href="#">About Us</a></li>
            <button><a href="#">SignIn</a></button>
            <button><a href="#">SignUp</a></button>
        </ul>
    </nav>

    <main>
        <section class="section1">
            <p>Picture or a background design.</p>
            <button>Get Started</button>
        </section>

        <section class="section2">
            <h2>Our Services</h2>
            <div class="services">
                <div class="service reveal">
                    <button><a href="#">Land</a></button>
                </div>
                <div class="service reveal">
                    <button><a href="#">Diseases</a></button>
                </div>
                <div class="service reveal">
                    <button><a href="#">Market</a></button>
                </div>
            </div>
        </section>
        <section class="section3">
            <h2>About</h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas sed diam eget risus varius blandit sit amet non magna.</p>
        </section>
    </main>

    <footer>
        <p>Contact Us</p>
    </footer>

    <script>
        const reveals = document.querySelectorAll('.reveal');

        const revealOptions = {
            threshold: 0.3,
            rootMargin: "0px 0px -50px 0px"
        };

        const revealOnScroll = new IntersectionObserver(function(entries, revealOnScroll) {
            entries.forEach((entry, index) => {
                if (!entry.isIntersecting) {
                    return;
                } else {
                    setTimeout(() => {
                        entry.target.classList.add('active');
                    }, index * 700);
                    revealOnScroll.unobserve(entry.target);
                }
            });
        }, revealOptions);

        reveals.forEach((reveal, index) => {
            revealOnScroll.observe(reveal);
        });
    </script>
"""

# Embed HTML content using Streamlit's HTML component
st.components.v1.html(home_form, height=1000)
