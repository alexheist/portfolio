import React from 'react';
import { Route, Link } from 'react-router-dom';
import Nav from './nav';

//const Slug = ({ match }) => <p>{match.params.slug}</p>

class Blog extends React.Component {
    render() {
//      console.log(this.props);
//      const { url } = this.props.match;
//      console.log(url);
        return (
            <div id="page-content">
                <Nav />
                <h1>Blog page</h1>
            </div>
        )
    }
}

export default Blog;
