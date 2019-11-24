import React from 'react';
import {
    Route,
    Link,
    Switch,
    BrowserRouter as Router
} from 'react-router-dom';
import Nav from './nav';
import CodeBlock from './codeblock';
const ReactMarkdown = require('react-markdown');

function Header() {
    return (
        <div id="hero">
            <svg id="top-right" version="1.1" xmlns="http://www.w3.org/2000/svg">
                <path d="M 0,0 L 40,0 L 40,40" fill="none" stroke="#D4D3FF" strokeWidth="20" />
            </svg>
            <svg id="bottom-left" version="1.1" xmlns="http://www.w3.org/2000/svg">
                <path d="M 0,0 L 0,40 L 40,40" fill="none" stroke="#D4D3FF" strokeWidth="20" />
            </svg>
            <h1>Alex Heist</h1>
            <p>Blogger</p>
        </div>
    )
}

class Article extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            article: []
        };
    }

    componentDidMount() {
        console.log(this.props);
        console.log(this.props.match);
        fetch("https://localhost/api/slug/"+this.props.match.params.slug)
        .then(response => response.json())
        .then(data =>  {
            console.log(data);
            this.setState({article: data});
        });
        console.log("TODO: fetch article if no article");
        console.log(this.state.article);
    }

    render() {
        return (
            <div id="blog-content">
                <Nav />
                <Header />
                <div id="article">
                    <div id="article-details">
                        <h1>{this.state.article.title}</h1>
                        <p>by {this.state.article.author_name}</p>
                        <small>{this.state.article.published}</small>
                    </div>
                    <img src={this.state.article.thumbnail} alt="Article Image" />
                    <ReactMarkdown
                        className="article-content"
                        source={this.state.article.markdown}
                        renderers={{ code: CodeBlock }}
                    />
                </div>
            </div>
        )
    }
}

export default Article;
