require(['jquery', 'backbone', 'icanhaz', "m/commits"], function($, Backbone, ich, Commits) {
    var c = new Commits;
    
    var l = function() {
        c.models.forEach(function(e) {
            e.getCommits().forEach(function(commit) {
                $("#recent-commits").append(ich.commit({repo: e.get("repo")["name"], message: commit["message"]}));
            });
        });
    }

    c.fetch({success: l});
});
