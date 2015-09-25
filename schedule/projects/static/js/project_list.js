var projects;
$(function() {
	var PageableProjects = Backbone.PageableCollection.extend({
		model: Project,
		url: urls.api.projects,
		state: {
			pageSize: 15
		},
		mode: "client" // page entirely on the client side
	});
	
	projects = new PageableProjects();
	
	var EditLinkCell = Backgrid.UriCell.extend({
		className: "edit-link-cell",
		target: "_self",
		render: function () {
			this.$el.empty();
		    var url = this.model.get("url");
		    var rawValue = this.model.get(this.column.get("name"));
		    var formattedValue = this.formatter.fromRaw(rawValue, this.model);
		    this.$el.append($("<a>", {
		      tabIndex: -1,
		      href: url,
		      title: this.title || formattedValue,
		      target: this.target
		    }).text(formattedValue));
		    this.delegateEvents();
		    return this;
		}
	});
	
	var columns = [
	    {name: "name", label: "Name",cell: EditLinkCell},
	    {name: "type", label: "Type",cell: Backgrid.StringCell},
	    {name: "contract", label: "Contract",cell: Backgrid.StringCell}
	];
	
		
	// Set up a grid to use the pageable collection
	var pageableGrid = new Backgrid.Grid({
		columns: columns,
		collection: projects
	});
		
	// Render the grid
	var $grid = $("#project-grid");
	$grid.append(pageableGrid.render().el)
		
	// Initialize the paginator
	var paginator = new Backgrid.Extension.Paginator({
		collection: projects
	});
		
	// Render the paginator
	$grid.after(paginator.render().el);
		
	// Initialize a client-side filter to filter on the client
	// mode pageable collection's cache.
	var filter = new Backgrid.Extension.ClientSideFilter({
		collection: projects,
		fields: ['name']
	});
		
	// Render the filter
	$grid.before(filter.render().el);
		
	// Add some space to the filter and move it to the right
	$(filter.el).css({float: "right", margin: "20px"});
		
	// Fetch data
	projects.fetch({reset: true});
});