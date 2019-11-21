import React from 'react';
import { Route, Link } from 'react-router-dom';
import Nav from './nav';

const Slug = ({ match }) => <p>{match.params.slug}</p>

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

class ArticleList extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            articles: [],
        };
    }

    componentDidMount() {
        fetch("https://localhost:1337/api/articles/")
        .then(response => response.json())
        .then(data =>  {
            this.setState({articles: data});
            console.log(data);
        });
    }

    render() {
        return (
            this.state.articles.map(article => (
                <a href={article.slug} class="article">
                    <img src={article.thumbnail} alt="Thumbnail image for article" />
                    <h2>{article.title}</h2>
                    <p>&rarr;</p>
                </a>
            ))
        )
    }
}

class Blog extends React.Component {
    render() {
        console.log(this.props);
        const { url } = this.props.match;
        console.log(url);
        return (
            <div id="blog-content">
                <Nav />
                <Header />
                <div id="article-list">
                    <ArticleList />
                </div>
            </div>
        )
    }
}

export default Blog;
