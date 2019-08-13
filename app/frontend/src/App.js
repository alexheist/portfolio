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
            <h1>Alex Heist</h1>
            <p>Software Developer</p>
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

class App extends React.Component {
    render() {
        return (
            <div id="page-content">
                <Nav />
                <Hero />
                <div id="main-content">
                    <Elevator />
                    <Contact />
                </div>
            </div>
        )
    }
}

export default App;
