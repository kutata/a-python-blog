<!DOCTYPE html>
<html>
<head>
<title>{{'' if not title else title+' - '}}{{siteName}}</title>
<meta charset="utf-8">
<meta content="Hello" name="description">
% if keywords:
<meta content="{{keywords}}" name="keywords">
% else:
<meta content="{{siteName}}" name="keywords">
% end


<link rel="shortcut icon" href="/public/assets/images/favicon.ico" />
<link rel="stylesheet" type="text/css" href="/public/assets/css/thxs.me.css" />
<script type="text/javascript">
(function() {if (!/*@cc_on!@*/0) return;var e = "abbr, article, aside, audio, canvas, datalist, details, dialog, eventsource, figure, footer, header, hgroup, mark, menu, meter, nav, output, progress, section, time, video".split(', ');var i= e.length;while (i--) {document.createElement(e[i])}})();
</script>
</head>
<body>
<header>
	<h1 class="title"><a href="/">Hello</a></h1>
	<p class="bio">{{bio}}</p>
</header>
