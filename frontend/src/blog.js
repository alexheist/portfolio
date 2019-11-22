import React from 'react';
import {
    Route,
    Link,
    Switch,
    BrowserRouter as Router
} from 'react-router-dom'
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
            articlesToShow: 3,
            expanded: false
        };

        this.showMore = this.showMore.bind(this);
    }

    componentDidMount() {
        fetch("https://localhost:1337/api/articles/")
        .then(response => response.json())
        .then(data =>  {
            this.setState({articles: data});
        });
    }

    showMore() {
        this.state.articlesToShow === 3 ? (
            this.setState({ articlesToShow: this.state.articles.length, expanded: true })
        ) : (
            this.setState({ articlesToShow: 3, expanded: false })
        )
    }

    render() {
        return (
            <div id="article-list">
                {this.state.articles.slice(0, this.state.articlesToShow).map(article => (
                    <Link exact={true} className="article-link" to={{pathname: "/blog/"+article.slug}}>
                        <img src={article.thumbnail} alt="Thumbnail image for article" />
                        <h2>{article.title}</h2>
                        <small>{article.published}</small>
                        <p>&rarr;</p>
                    </Link>
                ))}
                <a id="showMoreBtn" onClick={this.showMore}>
                    {this.state.expanded ? (
                        <span>Show Less</span>
                    ) : (
                        <span>Show More</span>
                    )}
                </a>
            </div>
        )
    }
}

class Article extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            article: [],
        };
        console.log(props);
    }

    render() {
        return (
            <h1>Article Page</h1>
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
                <Router>
                    <Switch>
                        <Route exact path="/blog" component={ArticleList} />
                        <Route path="/blog/:year/:month/:slug" component={Article} />
                    </Switch>
                </Router>
            </div>
        )
    }
}

export default Blog;
