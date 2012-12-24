require(['jquery', 'backbone', 'icanhaz', "m/commits"], function($, Backbone, ich, Commits) {
    var c = new Commits;
    
    var l = function() {
        var i=0;
        c.models.forEach(function(e) {
            e.getCommits().forEach(function(commit) {
                if(i < 10)
                    $("#recent-commits").append(ich.commit({repo: e.get("repo")["name"], message: commit["message"]}));
                i++;
            });
        });
    }

    c.fetch({success: l});
});
