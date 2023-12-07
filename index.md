---
layout: default
---
By Nikhil Chittaluru, Jack Hurst, Marissa Sorkin, Plamen Tassev

{::comment}
The Wonderful World of Pokemon
{:/comment}

<p style='margin: 1em'>
   We took a look at the top 8 Pokemon World Championship teams from the past decade to understand what makes them the very best. 
</p>

<p style='margin: 1em'>
   We used data scraped from both the Pokemon World Championship website which provides Species, Year, Ranks, and Positions, and Serebii.net, which is a Pokemon statistics website that describes the multivariate attributes of every existing Pokemon, like Name, Type, Attack, Defense, etc. Our project uses both datasets to visualize the key attributes that highly influence the result of pokemon battles, as well as the nuanced insights that are not immediately apparent by just looking at the data alone.
</p>

# Background

<p style='margin: 1em'>
   Let’s quickly explain Pokemon. This is a made-up data viz-themed Pokemon called J06. J06, like all Pokemon, has multiple attributes. We will be focusing on the type and stats. Each Pokemon has 6 stats and up to 2 types.
</p>

[tree diagram of the key attributes of pokemon]

<p style='margin: 1em'>
   For a Pokemon battle, the player chooses six Pokemon to battle against an opponent’s team of six. In a battle, players take turns prepping their Pokemon or damaging the opponent’s until one of the teams runs out of Pokemon.  Many factors influence who wins, but the most important are the stats and the types. 
</p>

<p style='margin: 1em'>
   Below, you can see every existing Pokemon released up until 2022. There are nearly one thousand different species of Pokemon, each with their own types and stats.
</p>

<div class='tableauPlaceholder' id='viz1701865356282' style='position: relative'>
   <noscript>
      <a href='#'>
         <img alt='PokeDex ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Po&#47;Pokemon_17014658048490&#47;PokeDex&#47;1_rss.png' style='border: none' />
      </a>
   </noscript>
   <object class='tableauViz'  style='display:none;'>
      <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
      <param name='embed_code_version' value='3' />
      <param name='site_root' value='' />
      <param name='name' value='Pokemon_17014658048490&#47;PokeDex' />
      <param name='tabs' value='no' />
      <param name='toolbar' value='yes' />
      <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Po&#47;Pokemon_17014658048490&#47;PokeDex&#47;1.png' />
      <param name='animate_transition' value='yes' />
      <param name='display_static_image' value='yes' />
      <param name='display_spinner' value='yes' />
      <param name='display_overlay' value='yes' />
      <param name='display_count' value='yes' />
      <param name='language' value='en-US' />
      <param name='filter' value='publish=yes' />
   </object>
</div>
<script type='text/javascript'>
   var divElement = document.getElementById('viz1701865356282');
   var vizElement = divElement.getElementsByTagName('object')[0];
   if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='827px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='827px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}
    var scriptElement = document.createElement('script');
   scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
   vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>

<p style='margin: 1em'>
   This one shows the team compositions of the top-8 WC teams. Only a fraction of the total set of pokemon is seen as “good enough” for the competitive scene. Let’s try to find out why.
</p>



{::comment}
Top 8 Teams 2014-2022
{:/comment}

<div class='tableauPlaceholder' id='viz1701876271285' style='position: relative; margin-left: -183px'>
   <noscript>
      <a href='#'>
         <img alt='Horizontal World Championship Teams (2) ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Po&#47;Pokemon_17014658048490&#47;HorizontalWorldChampionshipTeams2&#47;1_rss.png' style='border: none' />
      </a>
   </noscript>
   <object class='tableauViz'  style='display:none;'>
      <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
      <param name='embed_code_version' value='3' />
      <param name='site_root' value='' />
      <param name='name' value='Pokemon_17014658048490&#47;HorizontalWorldChampionshipTeams2' />
      <param name='tabs' value='no' />
      <param name='toolbar' value='yes' />
      <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Po&#47;Pokemon_17014658048490&#47;HorizontalWorldChampionshipTeams2&#47;1.png' />
      <param name='animate_transition' value='yes' />
      <param name='display_static_image' value='yes' />
      <param name='display_spinner' value='yes' />
      <param name='display_overlay' value='yes' />
      <param name='display_count' value='yes' />
      <param name='language' value='en-US' />
      <param name='filter' value='publish=yes' />
   </object>
</div>
<script type='text/javascript'>
   var divElement = document.getElementById('viz1701876271285');
   var vizElement = divElement.getElementsByTagName('object')[0];
   if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1366px';vizElement.style.height='795px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1366px';vizElement.style.height='795px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}
   var scriptElement = document.createElement('script');
   scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
   vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>

<p style='margin: 1em'>
   A vertically scrolling vatiation of this viz including a histogram can be found <a href='https://public.tableau.com/views/Pokemon_17014658048490/WorldChampionshipTeams' target='_blank'>here</a>. We can break our analysis down into two sections: Types and Stats.
</p>


{::comment}
Types
{:/comment}

<div class='tableauPlaceholder' id='viz1701874866052' style='position: relative; margin-left: -183px'>
   <noscript>
      <a href='#'>
         <img alt='Worlds Types ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Po&#47;Pokemon_17014658048490&#47;WorldsTypes&#47;1_rss.png' style='border: none' />
      </a>
   </noscript>
   <object class='tableauViz'  style='display:none;'>
      <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
      <param name='embed_code_version' value='3' />
      <param name='site_root' value='' />
      <param name='name' value='Pokemon_17014658048490&#47;WorldsTypes' />
      <param name='tabs' value='no' />
      <param name='toolbar' value='yes' />
      <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Po&#47;Pokemon_17014658048490&#47;WorldsTypes&#47;1.png' />
      <param name='animate_transition' value='yes' />
      <param name='display_static_image' value='yes' />
      <param name='display_spinner' value='yes' />
      <param name='display_overlay' value='yes' />
      <param name='display_count' value='yes' />
      <param name='language' value='en-US' />
      <param name='filter' value='publish=yes' />
   </object>
</div>
<script type='text/javascript'>
   var divElement = document.getElementById('viz1701874866052');
   var vizElement = divElement.getElementsByTagName('object')[0];
   if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1366px';vizElement.style.height='795px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1366px';vizElement.style.height='795px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}
   var scriptElement = document.createElement('script');
   scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
   vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>

<p style='margin: 1em'>
   This is a normal paragraph following a header. GitHub is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere.
</p>



<img src="./assets/type_popularity_area.png?raw=true" alt="Types Area Chart" title="Types Area Chart" style='display: block; margin: auto;'>


<p style='margin: 1em'>
   This is a normal paragraph following a header. GitHub is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere.
</p>



{::comment}
Line Chart
{:/comment}

<div class='tableauPlaceholder' id='viz1701911489909' style='position: relative'>
  <noscript><a href='#'><img alt='Story 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ra&#47;rank_17019114634400&#47;Story1&#47;1_rss.png' style='border: none' /></a></noscript>
  <object class='tableauViz'  style='display:none;'>
    <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
    <param name='embed_code_version' value='3' />
    <param name='site_root' value='' />
    <param name='name' value='rank_17019114634400&#47;Story1' />
    <param name='tabs' value='no' />
    <param name='toolbar' value='yes' />
    <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ra&#47;rank_17019114634400&#47;Story1&#47;1.png' />
    <param name='animate_transition' value='yes' />
    <param name='display_static_image' value='yes' />
    <param name='display_spinner' value='yes' />
    <param name='display_overlay' value='yes' />
    <param name='display_count' value='yes' />
    <param name='language' value='en-US' />
    <param name='filter' value='publish=yes' />
  </object>
</div>
<script type='text/javascript'>
  var divElement = document.getElementById('viz1701911489909');
  var vizElement = divElement.getElementsByTagName('object')[0];
  vizElement.style.width = '1000px';
  vizElement.style.height = '627px';
  var scriptElement = document.createElement('script');
  scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
  vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>

<p style='margin: 1em'>
   This is a normal paragraph following a header. GitHub is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere.
</p>



{::comment}
Stacks Story
{:/comment}

<div class='tableauPlaceholder' id='viz1701862572364' style='position: relative'>
   <noscript>
      <a href='#'>
         <img alt='Team Weaknesses Breakdown ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;FK&#47;FKBD6TMD4&#47;1_rss.png' style='border: none' />
      </a>
   </noscript>
   <object class='tableauViz'  style='display:none;'>
      <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
      <param name='embed_code_version' value='3' />
      <param name='path' value='shared&#47;FKBD6TMD4' />
      <param name='toolbar' value='yes' />
      <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;FK&#47;FKBD6TMD4&#47;1.png' />
      <param name='animate_transition' value='yes' />
      <param name='display_static_image' value='yes' />
      <param name='display_spinner' value='yes' />
      <param name='display_overlay' value='yes' />
      <param name='display_count' value='yes' />
      <param name='language' value='en-US' />
      <param name='filter' value='publish=yes' />
   </object>
</div>
<script type='text/javascript'>
   var divElement = document.getElementById('viz1701862572364');
   var vizElement = divElement.getElementsByTagName('object')[0];
   vizElement.style.width='1016px';vizElement.style.height='991px';
   var scriptElement = document.createElement('script');
   scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
   vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>

This is a normal paragraph following a header. GitHub is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere.

<p style='margin: 1em'>
   This is a normal paragraph following a header. GitHub is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere.
</p>



{::comment}
Big Viz Story
{:/comment}

<div class='tableauPlaceholder' id='viz1701882379324' style='position: relative'>
   <noscript>
      <a href='#'>
         <img alt='Stat Distributions by Type ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Po&#47;PokemonVis&#47;StatDistributions&#47;1_rss.png' style='border: none' />
      </a>
   </noscript>
   <object class='tableauViz'  style='display:none;'>
      <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
      <param name='embed_code_version' value='3' />
      <param name='site_root' value='' />
      <param name='name' value='PokemonVis&#47;StatDistributions' />
      <param name='tabs' value='no' />
      <param name='toolbar' value='yes' />
      <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Po&#47;PokemonVis&#47;StatDistributions&#47;1.png' />
      <param name='animate_transition' value='yes' />
      <param name='display_static_image' value='yes' />
      <param name='display_spinner' value='yes' />
      <param name='display_overlay' value='yes' />
      <param name='display_count' value='yes' />
      <param name='language' value='en-US' />
      <param name='filter' value='publish=yes' />
   </object>
</div>
<script type='text/javascript'>
   var divElement = document.getElementById('viz1701882379324');
   var vizElement = divElement.getElementsByTagName('object')[0];
   vizElement.style.width='1016px';vizElement.style.height='991px';
   var scriptElement = document.createElement('script');
   scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
   vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>

<p style='margin: 1em'>
   This is a normal paragraph following a header. GitHub is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere.
</p>



{::comment}
Scatter Ploy Story
{:/comment}

<div class='tableauPlaceholder' id='viz1701793861768' style='position: relative'>
   <noscript>
     <a href='#'>
       <img alt='Scatter Plots ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Po&#47;Pokemon_17014658048490&#47;ScatterPlotStory&#47;1_rss.png' style='border: none' />
     </a>
   </noscript>
   <object class='tableauViz'  style='display:none;'>
      <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
      <param name='embed_code_version' value='3' />
      <param name='site_root' value='' />
      <param name='name' value='Pokemon_17014658048490&#47;ScatterPlotStory' />
      <param name='tabs' value='no' />
      <param name='toolbar' value='yes' />
      <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Po&#47;Pokemon_17014658048490&#47;ScatterPlotStory&#47;1.png' />
      <param name='animate_transition' value='yes' />
      <param name='display_static_image' value='yes' />
      <param name='display_spinner' value='yes' />
      <param name='display_overlay' value='yes' />
      <param name='display_count' value='yes' />
      <param name='language' value='en-US' />
      <param name='filter' value='publish=yes' />
   </object>
</div>
<script type='text/javascript'>
  var divElement = document.getElementById('viz1701793861768');
  var vizElement = divElement.getElementsByTagName('object')[0];
  vizElement.style.width='1000px';vizElement.style.height='1027px';
  var scriptElement = document.createElement('script');
  scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
  vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>

<p style='margin: 1em'>
   This is a normal paragraph following a header. GitHub is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere.
</p>
