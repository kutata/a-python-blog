<div class="content entry-list">

% for p in posts:
  <article>
    <h1><a href="{{p['url']}}">{{p['title']}}</a></h1>
    <div class="entry-tag">Posted @ {{p['date']}}</div>
    <div class="entry-content">
      % if p['preview']:
      <div class="entry-preview">
        {{! p['preview']}}
      </div>
      % else:
        {{! p['content']}}
      % end
    </div>
  </article>
% end

</div>

%rebase layout
