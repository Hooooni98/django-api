# Admin
------
### Custom Admin Page
    1. create templates/admin/base.html
    2. change below root value
    3. run python3 manage.py collecstatic

### base.html
    {% extends 'admin/base.html' %} {% block extrahead %}{{ block.super }}{% csrf_token %}
    <style>
        html[data-theme="light"],
        /* Most customization is possible by modifying only the root part */
        :root {
        --primary: #79aec8;
        --secondary: #417690;
        --accent: #9c3531;
        --primary-fg: #3c1554;

        --body-fg: #333;
        --body-bg: #fff;
        --body-quiet-color: #666;
        --body-loud-color: #000;

        --header-color: #ffc;
        --header-branding-color: var(--accent);
        --header-bg: var(--secondary);
        --header-link-color: var(--primary-fg);

        --breadcrumbs-fg: #c4dce8;
        --breadcrumbs-link-fg: var(--body-bg);
        --breadcrumbs-bg: var(--primary);

        --link-fg: #417893;
        --link-hover-color: #036;
        --link-selected-fg: #5b80b2;

        --hairline-color: #e8e8e8;
        --border-color: #ccc;

        --error-fg: #ba2121;

        --message-success-bg: #dfd;
        --message-warning-bg: #ffc;
        --message-error-bg: #ffefef;

        --darkened-bg: #f8f8f8; /* A bit darker than --body-bg */
        --selected-bg: #e4e4e4; /* E.g. selected table cells */
        --selected-row: #ffc;

        --button-fg: #fff;
        --button-bg: var(--primary);
        --button-hover-bg: #609ab6;
        --default-button-bg: var(--secondary);
        --default-button-hover-bg: #205067;
        --close-button-bg: #747474;
        --close-button-hover-bg: #333;
        --delete-button-bg: #ba2121;
        --delete-button-hover-bg: #a41515;

        --object-tools-fg: var(--button-fg);
        --object-tools-bg: var(--close-button-bg);
        --object-tools-hover-bg: var(--close-button-hover-bg);

        --font-family-primary:
            -apple-system,
        --font-family-monospace:
            ui-monospace,
        }

    </style>
    {% endblock %}