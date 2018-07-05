<!DOCTYPE html>
<html>
<head>
% if title:
<title>{{'' if not title else title+' - '}}{{sitename}}</title>
% else:
<title>{{sitename}}</title>
% end
<meta charset="utf-8">
<meta content="Hello" name="description">
% if keywords:
<meta content="{{keywords}}" name="keywords">
% else:
<meta content="{{sitename}}" name="keywords">
% end
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<link rel="shortcut icon" href="/public/images/favicon.ico" />
<link rel="stylesheet" type="text/css" href="/public/css/thxs.me.css" />
<script type="text/javascript">
(function() {if (!/*@cc_on!@*/0) return;var e = "abbr, article, aside, audio, canvas, datalist, details, dialog, eventsource, figure, footer, header, hgroup, mark, menu, meter, nav, output, progress, section, time, video".split(', ');var i= e.length;while (i--) {document.createElement(e[i])}})();
</script>
</head>
<body>
<header>
	<h1 class="title"><a href="/">{{sitename}}</a></h1>
	<p class="bio">{{bio}}</p>
</header>
