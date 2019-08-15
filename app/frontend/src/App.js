import React from 'react';
import logo from './logo.svg';

function Nav() {
    return (
        <nav>
            <a href="https://github.com/alexheist">GitHub</a>
            <a href="https://linkedin.com/alexander-heist">LinkedIn</a>
        </nav>
    )
}

function Hero() {
    return (
        <div id="hero">
            <svg id="top-right" version="1.1" xmlns="http://www.w3.org/2000/svg">
                <path d="M 0,0 L 40,0 L 40,40" fill="none" stroke="#D4D3FF" stroke-width="20" />
            </svg>
            <svg id="bottom-left" version="1.1" xmlns="http://www.w3.org/2000/svg">
                <path d="M 0,0 L 0,40 L 40,40" fill="none" stroke="#D4D3FF" stroke-width="20" />
            </svg>
            <h1>Alex Heist</h1>
            <p>Software Developer</p>
        </div>
    )
}

function Elevator() {
    return (
        <div id="elevator">
            <p>
               There’s beauty in simplicity, but chaos is cathartic. I work
               with startups and small businesses building the web applications
               to help them succeed. I began writing software in 2016, and
               since then have developed in many different languages for both
               personal and professional projects.
            </p>
        </div>
    )
}

function Contact() {
    return (
        <form id="contact" method="post" action="">
            <h2>Contact Me</h2>
            <div id="name-field">
	            <label for="name">Name</label>
                <input type="text" id="name" name="name" />
            </div>
            <div id="email-field">
                <label for="email">Email</label>
                <input type="email" id="email" name="email" />
            </div>
            <div id="message-field">
                <label for="message">Message</label>
                <textarea name="message" id="message" rows="10" cols="50" />
            </div>
            <input id="form-submit" type="submit" value="Submit" />
        </form>
    )
}

class App extends React.Component {
    render() {
        return (
            <div id="page-content">
                <Nav />
                <Hero />
                <Elevator />
                <Contact />
            </div>
        )
    }
}

export default App;
