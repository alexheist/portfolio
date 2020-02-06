import React from "react";
import Nav from "./nav";
import CodeBlock from "./codeblock";
const ReactMarkdown = require("react-markdown");

function Header() {
  return (
    <div id="hero">
      <svg id="top-right" version="1.1" xmlns="http://www.w3.org/2000/svg">
        <path
          d="M 0,0 L 40,0 L 40,40"
          fill="none"
          stroke="#D4D3FF"
          strokeWidth="20"
        />
      </svg>
      <svg id="bottom-left" version="1.1" xmlns="http://www.w3.org/2000/svg">
        <path
          d="M 0,0 L 0,40 L 40,40"
          fill="none"
          stroke="#D4D3FF"
          strokeWidth="20"
        />
      </svg>
      <h1>Alex Heist</h1>
      <p>Blogger</p>
    </div>
  );
}

class Article extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      article: []
    };
  }

  componentDidMount() {
    fetch("https://localhost/api/published/" + this.props.match.params.slug)
      .then(response => response.json())
      .then(data => {
        this.setState({ article: data });
      });
    fetch(
      "https://localhost/api/published/" + this.props.match.params.slug + "/",
      {
        method: "PATCH",
        body: JSON.stringify({ article: this.props.match.params.slug }),
        headers: {
          "Content-Type": "application/json"
        }
      }
    );
  }

  render() {
    return (
      <div id="blog-content">
        <Nav />
        <Header />
        <div id="article">
          <div id="article-details">
            <h1>{this.state.article.title}</h1>
            <p>
              by {this.state.article.name_first} {this.state.article.name_last}
            </p>
            <small>{this.state.article.published}</small>
          </div>
          <img src={this.state.article.thumbnail} alt="Article Thumbnail" />
          <ReactMarkdown
            className="article-content"
            source={this.state.article.markdown}
            renderers={{ code: CodeBlock }}
          />
        </div>
      </div>
    );
  }
}

export default Article;
