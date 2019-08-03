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
            <h1>Alex Heist</h1>
            <p>Software Developer</p>
            <a class="clear-btn" href="https://github.com/alexheist">GitHub</a>
            <a class="clear-btn" href="https://linkedin.com/alexander-heist">LinkedIn</a>
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

class App extends React.Component {
    render() {
        return (
            <div>
                <Nav />
                <Hero />
                <Elevator />
            </div>
        )
    }
}

export default App;
