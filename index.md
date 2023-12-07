---
layout: default
---
By Nikhil Chittaluru, Jack Hurst, Marissa Sorkin, Plamen Tassev

<img src="https://upload.wikimedia.org/wikipedia/en/e/e8/Pok%C3%A9mon_World_Championships_logo.png" alt="Pokemon World Championship Logo" title="Pokemon World Championship Logo" style='display: block; margin: auto; width: 20%;'>

<p style='margin: 3em'>
   We took a look at the top 8 Pokemon World Championship teams from the past decade to understand what makes them the very best. 
</p>

<p style='margin: 3em'>
   We used data scraped from both the Pokemon World Championship website which provides Species, Year, Ranks, and Positions, and Serebii.net, which is a Pokemon statistics website that describes the multivariate attributes of every existing Pokemon, like Name, Type, Attack, Defense, etc. Our project uses both datasets to visualize the key attributes that highly influence the result of pokemon battles, as well as the nuanced insights that are not immediately apparent by just looking at the data alone.
</p>

# Background

<p style='margin: 3em'>
   Let’s quickly explain Pokemon. Each Pokemon has multiple attributes. We will be focusing on their types and stats. Each Pokemon has 6 stats and up to 2 types.
</p>

<p style='margin: 3em'>
   For a Pokemon battle, the player chooses six Pokemon to battle against an opponent’s team of six. In a battle, players take turns prepping their Pokemon or damaging the opponent’s until one of the teams runs out of Pokemon.  Many factors influence who wins, but the most important are the stats and the types. 
</p>

<p style='margin: 3em'>
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

<p style='display: block; margin: 1em; text-align: center; color: #6d6d6d; font-style: italic'>
   Icons of every existing Pokemon in order according to their National Number. Hover over one to see its attributes (Name, Number, Gen, Primary Type, Secondary Type, and Base Stats). Click a Pokemon to highlight others with the same type combination.
</p>

<p style='margin: 3em'>
   This one shows the team compositions of the top-8 WC teams. Only a fraction of the total set of pokemon is seen as “good enough” for the competitive scene. Let’s try to find out why.
</p>




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

<p style='display: block; margin: 1em; text-align: center; color: #6d6d6d; font-style: italic'>
   Table with the Pokemon on each Top-8 Team over for each World Championship. Hover over one to see its attributes (Name, Number, Primary Type, Secondary Type). Click a Pokemon to highlight other teams that used the same one. A vertically scrolling variation of this viz including a histogram can be found <a href='https://public.tableau.com/views/Pokemon_17014658048490/WorldChampionshipTeams' target='_blank'>here</a>. 
</p>


<p style='margin: 3em'>
   We can break our analysis down into two sections: Types and Stats.
</p>

# Types

<p style='margin: 3em'>
   Types are a major influence in a battle because they act as damage multipliers. Certain types are either:
</p>

<p style='margin: 1em; margin-left: 5em'>
   Not effective at all (x0): Does not damage the attacked Pokemon
</p>
<p style='margin: 1em; margin-left: 5em'>
   Not very effective (x0.5): Does half the damage to the attacked Pokemon
</p>
<p style='margin: 1em; margin-left: 5em'>
   Neutrally effective (x1.0): Does the normal damage to the attacked Pokemon
</p>
<p style='margin: 1em; margin-left: 5em'>
   Super effective (x2.0): Does double the damage to the attacked Pokemon
</p>


<p style='margin: 3em'>
   This type of matchup chart from Wikipedia highlights the “effectiveness” relationships between the attacking and defending types.
</p>

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Pokemon_Type_Chart.svg/1024px-Pokemon_Type_Chart.svg.png" alt="Types Matchup Chart" title="Types Matchup Chart" style='display: block; margin: auto; width: 50%;'>

<p style='display: block; margin: 1em; text-align: center; color: #6d6d6d; font-style: italic'>
   The table shows the damage multiplier based on the attacking and defending types. 0 indicates not effective, ½ indicates not very effective, blank indicates neutral effective, and 2 indicates super effective.
</p>


<p style='margin: 3em'>
   Let’s now look at which types are used in the WC scene. The treemap below gives a breakdown of the popular primary and secondary types used throughout the past decade.
</p>


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

<p style='display: block; margin: 1em; text-align: center; color: #6d6d6d; font-style: italic'>
   Treemap showing the most popular primary and secondary types by color. Hover over a square to see the exact type combination of each square (Primary and Secondary) as well as the number of WC Top-8 appearances. Click a square to see the corresponding square in the adjacent Treemap.
</p>

<p style='margin: 3em'>
   Both show that there are very common types (such as Fire, Electric, and Water) and not-so-popular types (Ice, Bug, and Fighting) in the WC tournaments. Looking back at the type chart, it makes sense that Ice and Bug types are not popular with all their weaknesses, but it does not easily explain why Electric types are so common. We believe these types, while not standing out in terms of “effectiveness”, have Pokemon that tend to have other great attributes.
</p>

<p style='margin: 3em'>
   Now we know which types are popular, but how do they change over time? The stream graph below shows how many of a certain type show up in the Top 8 each year.
</p>

<img src="./assets/type_popularity_area.png?raw=true" alt="Types Area Chart" title="Types Area Chart" style='display: block; margin: auto;'>

<p style='display: block; margin: 1em; text-align: center; color: #6d6d6d; font-style: italic'>
   Streamplot of the count of each type in the WC Top-8 over the years. Each color represents a unique type.
</p>

<p style='margin: 3em'>
   It shows how some types have become more and less popular. Water types have become very popular since 2016. Grass and Psychic are also on the rise. Dragon types, on the other hand, seem to disappear over the years. Looking at the type chart again, it seems that Fairy is the reason. Fairy is strong against Dragon, so as it becomes more popular, the effectiveness of Dragon types decreases. It is also easy to see that only about half of the types are seen in the competitive scene rather than all eighteen.
</p>

<p style='margin: 3em'>
   Let’s take it even further. What if we could see which types are the most dangerous (i.e., which types pose the greatest threat to a team)? Below is a collection of stacked bar charts showing how much of a weakness a team has towards a specific type.
</p>


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

<p style='display: block; margin: 1em; text-align: center; color: #6d6d6d; font-style: italic'>
   Stacked bar chart showing 1) the average weakness level across a WC tournament against a specific type and 2) the team-specific weakness level in a WC tournament against a specific type. Each level is based on a type's damage multiplier against a specific Pokemon in the team (0 = not effective, 0.5 = not very effective, …, 4 = double super effective). Each color represents an individual Pokemon at a certain position. Hover over a square to see the position and multiplier. Click the Year drop-down to select ‘All’ years or choose a specific year. Click the Rank drop-down to select a specific rank in a specific year or ‘All’ to see the average weakness level for that year.
</p>

<p style='margin: 3em'>
   This chart collection illuminates a few interesting trends. In the “Weaknesses by Year” chart, overall, it seems there is an even weakness distribution across all types, with peaks at Ice, Ground, and Rock and valleys at Normal and Bug. This follows the type chart pretty well. 
</p>


<p style='margin: 3em'>
   However, since roughly half of the types are used, there are unique breakdowns for weaknesses year by year. For example, 2022 has a particularly high weakness to Poison and a much higher resistance to Ground types. Furthermore, looking back at the stream graph, Both Poison and Ice types were non-existent that year. Is this because the small set of “competitively viable” Pokemon can ignore the less popular types, or is it by design as the “dangerous” types have very few strong Pokemon, or is it simply a coincidence? 
</p>


<p style='margin: 3em'>
   Examining the individual rank weaknesses, it seems that the weaknesses of the top 8 vary drastically across the teams. Despite only drawing from this small set, it seems that subtle differences in team composition heavily influence the weaknesses distribution of the individual teams. Based on 2022’s Rank 1 distribution, having resistance to fire, flying, electric, and psychic gives you a great advantage over the competition. 
</p>

# Stats

<p style='margin: 3em'>
   Stats also influence the damage multipliers in a battle, along with the battle duration and priority. Each Pokemon has 6 stats:
</p>

<p style='margin: 1em; margin-left: 5em'>
   HP: The health points of a Pokemon
</p>
<p style='margin: 1em; margin-left: 5em'>
   Atk: The physical attack of a Pokemon
</p>
<p style='margin: 1em; margin-left: 5em'>
   Def: The physical defense of a Pokemon
</p>
<p style='margin: 1em; margin-left: 5em'>
   Sp. Atk: The special attack of a Pokemon
</p>
<p style='margin: 1em; margin-left: 5em'>
   Sp. Def: The special defense of a Pokemon
</p>
<p style='margin: 1em; margin-left: 5em'>
   Spd: The speed of a Pokemon
</p>



<p style='margin: 3em'>
   Damage is done by taking away HP from a Pokemon. Once its HP is reduced to 0, the Pokemon is no longer usable in that battle. Along with the type “effectiveness” multiplier, the damage is multiplied by the ratio of the attacking Pokemon’s attack stat to the defending Pokemon’s defense stat (Atk/Def). A Pokemon can either attack with a physical or special attack. The corresponding defense stat of the attacked Pokemon is used in the ratio. Speed determines which Pokemon moves attacks first for each turn, with the higher-speed Pokemon moving first.
</p>

<p style='margin: 3em'>
   All in all, pokemon having high stats tends to mean they are good. Let’s look at some trends. Below is the average of the stats of the top 8 teams over the years.
</p>



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

<p style='display: block; margin: 1em; text-align: center; color: #6d6d6d; font-style: italic'>
   1) Line chart showing the average stats of the Top-8 WC teams for each year and 2) Bar Chart showing average stats of each of the Top-8 WC teams by year. Hover over a line or bar to see the specific value. On chart 2) click the Year drop-down to select a specific year or ‘Null’ to see the average stats across all Pokemon.
</p>

<p style='margin: 3em'>
   This chart shows the average of each stat for the top 8 teams for each year. Attack is preferred across the board and is approximately 10% higher than the other stats. Special Attack catches up in 2022, but prioritizing one of the Attack stats is the best option when choosing Pokemon for a team. 
</p>

<p style='margin: 3em'>
   There also seems to be an almost periodic behavior between the rest of the stats peaking and dropping every couple of years. We think this is due to the new Pokemon added each year that change the meta for the game. GameFreak, the owners of Pokemon, tend to add or change game factors every year. These changes influence the damage calculation. For example, the stats peaked in 2019 and dropped in 2020 because of a controversial change called “Dexit.” This change caused many of the older Pokemon to be inaccessible in the new game used for the competition. Looking at the team composition in the top table, none of the Pokemon used in 2019 were used in 2020. Due to this new rule, there are very few repeated icons. The change was reverted in 2022, and the overall stats increased.
</p>

<p style='margin: 3em'>
   Next, let’s look at the stat broken down across the ranks. There seem to be few trends in this chart. While there are minor differences between the individual stats, they are all relatively the same level. The main takeaway we see is similar to the “Stats Combined” chart. WC-level teams prioritize high attack stats over all others. In 2022, it seems that special defense is preferred over physical defense, and physical attack is preferred over special attack.
</p>

# Roles

<p style='margin: 3em'>
   Let's take this one step further. In the competitive scene, the 6 Pokemon tend to have a role. Some of the roles include:
</p>
<p style='margin: 1em; margin-left: 5em'>
   Leads (Def & Spd): These Pokemon are sent out first to battle so they need to be fast to first move and endure an attack from the opponent if needed.
</p>
<p style='margin: 1em; margin-left: 5em'>
   Walls (HP & Def): These Pokemon specialize in setups by withstanding multiple attacks from the opponent until they are ready to make a move.
</p>
<p style='margin: 1em; margin-left: 5em'>
   Wall Breakers(Atk & Def): These Pokemon are great for stopping Walls before they can set up and make their move.
</p>
<p style='margin: 1em; margin-left: 5em'>
   Bulk Sweepers(HP & Atk): These Pokemon are great at withstanding a few attacks from opponents but can specialize in taking out opponents quickly.
</p>
<p style='margin: 1em; margin-left: 5em'>
   Fast Sweepers(Atk & Spd): These Pokemon are very fast and aim to attack and take out the opponent before they get hit themselves.
</p>

<p style='margin: 3em'>
   A team’s role composition depends on each player’s play style. Since varying roles allow teams to adapt to others, these roles are an important part of the competitive Pokemon scene. To better understand which Pokemon are good at each listed role, we made a scatterplot showing the two key stats on each axis. 
</p>

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

<p style='display: block; margin: 1em; text-align: center; color: #6d6d6d; font-style: italic'>
   A scatterplot compares two specific stats based on the five selected roles: 1) Leads, 2) Walls, 3) Wall Breakers, 4) Bulk Sweepers, and 5) Fast Sweepers. Physical and Special Attacks are combined into Attack, while Physical and Special Defense are combined into a Defense. Darker shading means more World Appearances. Hover over a silhouette to see its attributes (Name, Number, World Appearances, and Stats). Use the Primary Type and Secondary Type drop-downs to select a specific type combination or select ‘All’ to see every Pokemon in that category.
</p>


<p style='margin: 3em'>
   The darker silhouettes demonstrate the number of occurrences the Pokemon has on the WC top-8 stage. The most used Pokemon lie near the diagonal of the scatterplot, farther away from the origin. This viz gives a better idea of which Pokemon are better at a certain role (closer to the diagonal).
</p>

<p style='margin: 3em'>
   The outliers in these plots are usually the Pokemon, who has a better-suited role. However, the ones that lie on the diagonal but are closer to the origin tend to have unique abilities that boost their stats. For example, the Rotom base form is relatively close to the center for a WC Pokemon. It has an inherent ability to transform and boost its stats. This transformed form is what competitive teams use in battle.
</p>

# Types & Stats

<p style='margin: 3em'>
   After seeing the trends in the types and stats of the top 8 separately, let’s combine them into a single viz to see any interesting features. 
</p>

<p style='margin: 3em'>
   Before that, let’s quickly explain “legendaries.” There is a class of Pokemon called “legendary” as part of the game's lore. These “legendary” Pokemon tend to have extremely high stats across the board. There is another term known as “pseudo-legendary,” which refers to Pokemon that are not technically “legendary” but have stats similar to one. Both “legendary” and “pseudo-legendary” pokemon have a sum of stats greater than 600. Pokemon near or above this 600 threshold are common on WC teams.
</p>

<p style='margin: 3em'>
   Now, let’s look at the overall distribution. Below are two dot plots showing each Pokemon's stat distribution by type.
</p>

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

<p style='display: block; margin: 1em; text-align: center; color: #6d6d6d; font-style: italic'>
   Dot plot distribution for Pokemon based on the 1) Sum of Stats and 2) Individual Stats. Each distribution is also grouped into rows by Primary Type. The dark vertical line represents the median value of the row. The dotted lines represent -1σ and +1σ around the mean of the row. Hover or Click a line to see the exact value. Hover over a dot to see its attributes (Name, Primary Type, World Appearances). The size and color of the dots both correspond to the number of World Appearances made by that Pokemon. Click the Year drop-down to filter the WC years to consider (leave ‘Null’ selected to see the WC Pokemon compared to every other Pokemon). 
</p>

<p style='margin: 3em'>
   The “Sum of Stats” dot plot shows many of the WC Pokemon are near this 600 stat level. The ones that do not tend to be well above the median sum of stats for the type. The outliers of these two sets are worth noting. These Pokemon typically have a special strategy based on their moves and abilities. One example is the normal-type Pokemon Smeargle, which has a strategy based around its unique move called “Sketch.” 
</p>

<p style='margin: 3em'>
   On the flip side, the Pokemon to the far right (above the 600 stat level) that are not seen in the WC scene have reasons for not being utilized. One example of this is the normal-type Pokemon Slaking. Although its stats are very high, it has an ability called “Truant” that prevents it from making a move every other turn. An ability like that is detrimental in the WC scene.
</p>


<p style='margin: 3em'>
   In the “Individual Stats” dot plot, we can see how the popular WC Pokemon compares to the overall set of Pokemon. It is clear where the top Pokemon excel, and looking closely enough, team roles pop out based on how their base stats compare to the median. Like in the “Sum of Stats” plot, the outliers are worth noting. Blissey(a normal type) or Shuckle(a bug type) have extremely high stats in certain categories. But clicking them reveals that they have quite underwhelming stats in others.
</p>

# Conclusion

<p style='margin: 3em'>
   Our comprehensive analysis of the top 8 teams from the past decade of Pokemon World Championships has unveiled a wealth of insights into the strategies and compositions that make these teams successful. Through our detailed examination of types, stats, and roles, several key themes have emerged:
</p>

<p style='margin: 1em; margin-left: 5em'>
   <b>Type Matters:</b> The prevalence of certain types over others in championship teams underscores the importance of understanding and exploiting type matchups. Notably, types like Water, Electric, and Fire have dominated, while Ice, Bug, and Fighting types have been less common.
</p>
<p style='margin: 1em; margin-left: 5em'>
   <b>Stat Prioritization:</b> High Attack stats have consistently been a hallmark of top-performing teams. This emphasizes the competitive advantage of offensive strategies over defensive ones in the championship meta.
</p>
<p style='margin: 1em; margin-left: 5em'>
   <b>Role Diversification:</b> Successful teams have demonstrated a balanced mix of roles, adapting to various battle scenarios. Roles such as Leads, Walls, Wall Breakers, Bulk Sweepers, and Fast Sweepers are crucial for a well-rounded team capable of handling diverse threats.
</p>
<p style='margin: 1em; margin-left: 5em'>
   <b>Evolving Meta:</b> The fluctuating popularity of certain types and stats over the years reflects the evolving nature of competitive Pokemon. This highlights the necessity for players to stay adaptable and up-to-date with the changing meta.
</p>
<p style='margin: 1em; margin-left: 5em'>
   <b>The Role of 'Legendary' and 'Pseudo-Legendary' Pokemon:</b> These Pokemon often play a significant role in top teams, given their superior stats. However, our analysis also revealed that some Pokemon with high stats are overlooked due to certain detrimental abilities or lack of versatility in roles.
</p>
<p style='margin: 1em; margin-left: 5em'>
   <b>Outlier Strategies:</b> We noticed that some teams succeeded with unconventional strategies, utilizing Pokemon that don't fit the typical high-stat mold. This suggests that creativity and surprise elements can be as effective as conventional strategies.
</p>
<p style='margin: 3em'>
   In summary, our project illuminates the complex interplay of types, stats, and roles in shaping the strategies of top Pokemon World Championship teams. While certain patterns and preferences are clear, the dynamic nature of competitive Pokemon means that adaptability, innovative team composition, and a deep understanding of the game's mechanics are key to success.
</p>


<p style='margin: 3em'>
   As the Pokemon landscape continues to evolve, future competitors can draw upon these insights to craft their strategies. Whether through embracing tried-and-tested methods or pioneering new approaches, the world of competitive Pokemon remains a vibrant and challenging arena.
</p>
