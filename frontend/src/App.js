import React from 'react';

function Nav() {
    return (
        <nav>
            <a href="https://github.com/alexheist">GitHub</a>
            <a href="https://linkedin.com/in/alexander-heist">LinkedIn</a>
        </nav>
    )
}

function Hero() {
    return (
        <div id="hero">
            <svg id="top-right" version="1.1" xmlns="http://www.w3.org/2000/svg">
                <path d="M 0,0 L 40,0 L 40,40" fill="none" stroke="#D4D3FF" strokeWidth="20" />
            </svg>
            <svg id="bottom-left" version="1.1" xmlns="http://www.w3.org/2000/svg">
                <path d="M 0,0 L 0,40 L 40,40" fill="none" stroke="#D4D3FF" strokeWidth="20" />
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

class Contact extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            name: "",
            email: "",
            message: "",
        };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(id) {
        let label = document.getElementById(id);
        let input = document.getElementById(id.slice(0,-6));
        if (input.value.length > 0 && window.innerWidth > 768 ) {
            label.setAttribute('style', 'color: transparent');
            label.innerHTML = input.name.charAt(0).toUpperCase() + input.name.slice(1);
            input.setAttribute('style', 'border-color: #CCCCCC;');
        } else {
            label.setAttribute('style', 'color: #656565');
        }
        this.setState({
            [input.name]: input.value
        });
        document.getElementById("success-response").innerHTML = "";
    }

    handleSubmit(event) {
        event.preventDefault();

        let clearForm = () => {
            document.getElementById("name").value = '';
            document.getElementById("email").value = '';
            document.getElementById("message").value = '';
            if (window.innerWidth > 768 ) {
                document.getElementById("name-label").setAttribute('style', 'color:#656565;');
                document.getElementById("email-label").setAttribute('style', 'color:#656565;');
                document.getElementById("message-label").setAttribute('style', 'color:#656565;');
            }
        }

        var data = JSON.parse(JSON.stringify({
            "name": this.state.name,
            "email": this.state.email,
            "message": this.state.message,
        }))

        window.grecaptcha.ready(function() {
            window.grecaptcha.execute(
                "6Lf676IUAAAAADMzDrQ0Quakf2KPsrHyDWT15snH",
                {action: 'homepage'}
            ).then(function(token){
                data.recaptchaToken = token;
                data = JSON.stringify(data);
                fetch("http://localhost:8000/api/leads/",
                    {
                        method: "POST",
                        body: data,
                        headers: {
                            "Content-Type": "application/json"
                        }
                    }
                )
                .then(response => response.json())
                .then(response =>  {
                    if (typeof response === 'object' && response !== null) {
                        var input = document.getElementById(Object.keys(response)[0]);
                        var label = document.getElementById(Object.keys(response)[0]+'-label');
                        label.innerHTML = Object.values(response)[0][0];
                        label.setAttribute('style', '');
                        input.value = '';
                        input.setAttribute('style', 'border-color: red;');
                    }
                    if (response === 201) {
                        clearForm();
                        document.getElementById("success-response").innerHTML = "<p>Thank you, I will be in touch shortly</p>";
                    } else if (response === 200) {
                        clearForm();
                        document.getElementById("success-response").innerHTML = "<p>Thank you</p>";
                    }
                })
            });
        });
    }

    render () {
        return (
            <form id="contact" onSubmit={this.handleSubmit}>
                <h2>Contact Me</h2>
                <div id="name-field">
                    <label id="name-label" htmlFor="name">Name</label>
                    <input type="text" id="name" name="name" onChange={() => this.handleChange("name-label")} />
                </div>
                <div id="email-field">
                    <label id="email-label" htmlFor="email">Email</label>
                    <input type="email" id="email" name="email" onChange={() => this.handleChange("email-label")} />
                </div>
                <div id="message-field">
                    <label id="message-label" htmlFor="message">Message</label>
                    <textarea name="message" id="message" rows="10" cols="50" onChange={() => this.handleChange("message-label")} />
                </div>
                <input id="form-submit" type="submit" value="Submit" />
                <span id="success-response"></span>
                <p id="recaptchaBranding">
                    This site is protected by reCAPTCHA and the Google <a href="https://policies.google.com/privacy">Privacy Policy</a> and <a href="https://policies.google.com/terms">Terms of Service</a> apply.
                </p>
            </form>
        );
    }
}

class App extends React.Component {
    componentDidMount() {
        const script = document.createElement('script')
        script.src = `https://www.google.com/recaptcha/api.js?render=6Lf676IUAAAAADMzDrQ0Quakf2KPsrHyDWT15snH`;
        document.body.appendChild(script);
    }

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
