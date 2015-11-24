var SearchBar = React.createClass({
    displayName: 'SearchBar',
    render: function () {
    	var rawMarkup = this.props.children;
        return (
            <div>
            	<input type="text" class="search">
            </div>
        );
    }
});

var SearchResult = React.createClass({
    displayName: 'SearchResult',
    getInitialState: function () {
        return {
            data: {
                "url" : "search above"
            }
        }
    },
    render: function () {
        var rawMarkup = this.props.children;
        return (
            <div>
                <p>{this.state.data.url}</p>
            </div>
        );
    }
});

var Article  = React.createClass({
	displayName: 'Article',
	getInitialState: function (){
		return {
			data: {
				"title":"Loading...", 
				"url": ".",
				"content": "..."}
			};
	},
	handleArticleLoad: function (){
		this.clearVoteStatus();
		this.setState(this.getInitialState());
	},
	loadArticleFromServer: function(){
		this.handleArticleLoad();
		$.ajax({
			url: "article",
			dataType: "json",
			success: function(data){
				this.setState({data:data});
			}.bind(this),
			error: function(xhr, status, err){
				console.error("article GET failed", status, err.toString());
			}.bind(this)
		});
	},
	componentDidMount: function() {
		//this.loadArticleFromServer();
	},
    render: function () {
    	var classString = "col-md-6 article " + this.state.voteStatus;
        return (
        	<div className={classString}>
            	<h1> {this.state.data.title} </h1>
            	<ArticleContent>{this.state.data.content}</ArticleContent>
            </div>
        );
    }
});

var Container = React.createClass({
    displayName: 'Container',
    render: function () {
        return (
        	<div className="row">
	            <SearchBar> </SearchBar>
                <SearchResult> </SearchResult>
            </div>
        );
    }
});

React.render(
	<Container onKeyDown={this.handleKeyPress} />,
	document.getElementById('content')
);