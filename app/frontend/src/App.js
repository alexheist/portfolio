import React from 'react';
import logo from './logo.svg';
import './App.css';

function Nav() {
    return (
        <nav>
            <a href="#about-me">About Me</a>
            <a href="#projects">Projects</a>
            <a href="#contact">Contact</a>
        </nav>
    )
}

function Hero() {
    return (
        <div id="hero">
            <div id="hero-content">
                <h1>Alex Heist</h1>
                <p>Software Developer</p>
                <a class="clear-btn" href="https://github.com/alexheist">GitHub</a>
                <a class="clear-btn" href="https://linkedin.com/alexander-heist">LinkedIn</a>
            </div>
        </div>
    )
}

function Elevator() {
    return (
        <div id="elevator">
            <p>There's beauty in simplicity, but chaos is cathartic. I work with startups, and have developed many of their applications. I began writing software in 2016 and since then have programmed in many different languages for both personal and professional projects</p>
        </div>
    )
}

function Projects() {
    return (
        <div id="projects">
            <h2>My Projects</h2>
            <img src="https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwjFivTV4-jAhUiGTQIHb1xAQQQjRx6BAgBEAQ&url=https%3A%2F%2Floremipsum.io%2F21-of-the-best-placeholder-image-generators%2F&psig=AOvVaw3NxYpHwZCO1CVtCW9SBo3O&ust=1565233589685635" />
            <h5>Project Name</h5>
            <p>Some information about the project that I came up with on a whim</p>
        </div>
    )
}

function Contact() {
    return (
        <div id="contact">
            <h2>Contact Me</h2>
            <form method="post" action="">
                <label for="name">Name</label>
                <input type="text" id="name" name="name" />
                <label for="email">Email</label>
                <input type="email" id="email" name="email" />
                <label for="message">Message</label>
                <textarea name="message" id="message" rows="10" cols="50" />
                <input type="submit" value="Submit" />
            </form>
        </div>
    )
}

function Footer() {
    return (
        <footer>
            <p>Alex Heist</p>
        </footer>
    )
}

class App extends React.Component {
    render() {
        return (
            <div>
                <Nav />
                <Hero />
                <div id="main-content">
                    <Elevator />
                    <Projects />
                    <Contact />
                </div>
                <Footer />
            </div>
        )
    }
}

export default App;
