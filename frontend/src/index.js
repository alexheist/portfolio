import React from 'react';
import ReactDOM from 'react-dom';
import {
    Route,
    Link,
    Switch,
    BrowserRouter as Router
} from 'react-router-dom'
import Landing from './landing';
import Blog from './blog';
import Article from './article';
import NotFound from './notfound';
import './index.css';
import './blog.css';

const routing = (
    <Router>
        <div>
            <Switch>
                <Route exact path="/" component={Landing} />
                <Route path="/blog/:slug" component={Article} />
                <Route exact path="/blog" component={Blog} />
                <Route component={NotFound} />
            </Switch>
        </div>
    </Router>
)

ReactDOM.render(routing, document.getElementById('root'));
