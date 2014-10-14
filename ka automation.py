"""
ka design automation tools - 
super rough, but this is a set of functions, documented at the bottom, 
which let you get the text/names of topics/subjects/domains for parts of 
our topic tree.

you need to get the topic tree, which you can do by running
    
    curl -o ~/topictree.json http://www.khanacademy.org/api/v1/topictree
    
good luck!
"""

size(2048, 1536)
background(None)

topics = read("~/topictree.json")
# print topics.keys()

# get subjects
domains = topics['children']

# a list of the human readable subjects
domain_names = [t['title'] for t in domains]
domain_slugs = [t['slug'] for t in domains]
domain_list = [(t['title'], t['slug']) for t in domains]

def subjects_for_domain(slug):
    subjects = [t['children'] for t in domains 
                    if t['domain_slug'] == slug]
    if subjects:
        return subjects[0]

def topic_color_for(slug):
    colors = {u'coach-res': '#5cd0b3', 
    u'new-and-noteworthy': '#5cd0b3', 
    u'computing': '#83c167', 
    u'science': '#c55f73', 
    u'talks-and-interviews': '#5cd0b3', 
    u'humanities': '#fc6255', 
    u'partner-content': '#5cd0b3', 
    u'economics-finance-domain': '#f0ac5f', 
    u'test-prep': '#9a72ac', 
    u'math': '#4fbad4'}
    return colors.get(slug, '#5cd0b3')

def subject_color_for(slug):
    colors = {
        u'computing': '#76af5c', 
        u'science': '#9c4959', 
        u'humanities': '#e5594b', 
        # u'partner-content': '#48a78e', 
        u'partner-content': '#54c0a6', 
        u'economics-finance-domain': '#e0a057', 
        u'test-prep': '#7d5e8d', 
        u'math': '#45a7be'
    }
    return colors.get(slug, '#4c6678')

def domain_color_for(slug):
    colors = {
        u'computing': '#689b51', 
        u'science': '#93414e', 
        u'humanities': '#ce4f43', 
        # u'partner-content': '#48a78e', 
        u'partner-content': '#48a78e', 
        u'economics-finance-domain': '#c68c45', 
        u'test-prep': '#634071', 
        u'math': '#1b7489'
    }
    return colors.get(slug, '#304352')

def stripe_domain(domain):
    #draw progressively darker stripes of a color with subjects in a domain
    bgcolor = color(topic_color_for(domain))
    font_size = 14
    box_size = 54
    darkening = 0.6
    tint_quantity = darkening / len(subjects_for_domain(domain))

    bgcolor.v -= darkening
    for (i, s) in enumerate(subjects_for_domain(domain)):
        align(LEFT)
        font("Proxima Nova Semibold", font_size)
        bgcolor.v += tint_quantity
        
        fill(bgcolor)
        rect(0,box_size*i, 1024, box_size)
        fill(1)
        text(str(s['title']), 24, i * box_size + 24)

def color_domains():
    # returns all domains colored in their respective domain colors
    for d in domains:
        fill(subject_color_for(d['domain_slug']))
        align(CENTER)
        text(d['title'], 150, 100)
        line()

def get_topics(**kwargs):
    """ gets a list of topics in a subject
    
    **kwargs
    
    - domain: restricts chosen subject to domain
    - subject: returns topics within a given subject
    """
    import random
    domain_slugs = [t['slug'] for t in domains]
    domain_slug = kwargs.get('domain', random.choice(domain_slugs))
    # domain_title = TODODODODODODO
    
    subject_slugs = [s['slug'] for s in subjects_for_domain(domain_slug)]
    subject_slug = kwargs.get('subject', random.choice(subject_slugs))
    # subject_title = TODODODODODODODO
    
    # TODO: fix this to validate that args actually exist, only random
    # choices are guaranteed to exist
    subject = filter(lambda x: x['slug'] == subject_slug, 
        subjects_for_domain(domain_slug))
    # print domain_slug
    # print subject_slug
    ## number of topics we'll see
    # print len(subject[0]['children'])
    return subject[0]['children']
    pass


## print all domains (math/science/etc)
# for t in domains:
#     print t['slug']


## print all math subjects (separated by '          ')
import json

# print json.dumps([t['slug'] for t in subjects_for_domain('math')])

## print topics in seventh grade math
# for t in get_topics(domain='math', subject='cc-seventh-grade-math'):
#     print t['title']

## print topics and tutorials in seventh grade math
# for t in get_topics(domain='math', subject='cc-seventh-grade-math'):
#     print "\n%s" % t['title']
#     for tut in t['children']:
#         print "  " +  "--".join(["( )" for c in tut['children']]) + "  " + tut['title']

## print the id for each topic in math (this went nowhere) 
# print get_topics(domain='math', subject='cc-seventh-grade-math')[0].keys()
# for s in get_topics(domain='math', subject='cc-seventh-grade-math'):
#     print s.get('id')

## count amount of content in a given subject
# for s in subjects_for_domain('math'):
#     count = 0
#     for t in get_topics(domain='math', subject=s['slug']):
#         for tut in t['children']:
#             count += len(tut['children']) if tut.get('children') else 0
#     print json.dumps({'name': s['title'], 'size': count})


## print topics in a random math mission
# for t in get_topics(domain='math'):
#     print t['title']

## print topics in a random domain
# for t in get_topics(domain='math'):
#     print t['title']

# print subject/slug pairs for math
# for s in subjects_for_domain('math'):
#     print "%s: %s" % (s.get('title'), s.get('slug'))





def random_domain_color(slug, **kwargs):
    import random

    seed = kwargs.get('seed', 53)
    random.seed(seed)
    subject_count = len(subjects_for_domain(slug))
    darkening = 0.3
    tint_quantity = darkening / len(subjects_for_domain(slug))

    colors = [color(subject_color_for(slug)) for x in range(subject_count)]
    for i, c in enumerate(colors):
        c.v += i * tint_quantity
    
    random.shuffle(colors)
    return colors


def subject_box(title, box_fill, stylename, **kwargs):
    box_height = kwargs.get('height', 100)
    stroke_width = kwargs.get('stroke_width', 0)
    min_width = kwargs.get('min_width', 200)
    padding = {'right': 40, 'left': 6, 'bottom': 8}
    padding.update(kwargs.get('padding', {}))

    fill(1)
    label = text(title, padding['left'], box_height - padding['bottom'], style=stylename, plot=False)
    label_width = measure(label).width
    box_width = label_width + padding['right']
    if min_width:
        box_width = max(min_width, box_width)
    if stroke_width:
        stroke(1)
        strokewidth(stroke_width)
    fill(box_fill)
    rect(0, 0, box_width, box_height)
    plot(label)
    return box_width, box_height


stylesheet("subject", "proxima nova", "regular", 14)
stylesheet("domain", "proxima nova", "thin", 32)
stylesheet("subjecthead", "proxima nova", "light", 18)
def horizontal_grid(**kwargs):
    """prints a grid of horizontally scrubbable subjects and domains"""
    y_pos = 0
    seed = kwargs.get('seed')
    expand = kwargs.get('expand')
    for domain_title, domain in domain_list[1:]:
        x_pos = 0
        box_height = 0
        default_width = kwargs.get('default_width', 150)
        subject_area = 1024
        
        with translate(x_pos, y_pos):
            w, h = subject_box(domain_title, subject_color_for(domain), "domain", 
                                min_width=None, padding={'right': 80})
            x_pos += w

        if expand:
            subject_area -= x_pos
            subject_count = len(subjects_for_domain(domain))
            if subject_area - subject_count * default_width > 0:
                default_width = subject_area / subject_count
        
        for i, s in enumerate(subjects_for_domain(domain)):
            with translate(x_pos, y_pos):
                w, h = subject_box(s.get('title'), 
                                    random_domain_color(domain, seed=seed)[i], 
                                    "subject",
                                    min_width=default_width)
                x_pos += w
                box_height = h
        y_pos += box_height

# horizontal_grid(seed=51, expand=True)




def progress(x, y, **kwargs):
    """generates a circle with progress listed
    """
    import random
    INNER_RADIUS = 35
    OUTER_RADIUS = 1.25 * INNER_RADIUS
    STROKE_WIDTH = .04 * INNER_RADIUS * 2
    
    arc(x, y, INNER_RADIUS, range=360, fill=0.95,
        stroke=.7, strokewidth=STROKE_WIDTH)
    arc(x, y, OUTER_RADIUS, range=360, fill=None,
        stroke=.95, strokewidth=STROKE_WIDTH)
    
    prog_pct = kwargs.get('prog', random.uniform(5, 95))
    prog_amount = 360.0 * prog_pct / 100

    font("Proxima Nova", "Regular", 18)
    align(CENTER)
    text("%d%%" % (prog_pct), x+3, y+7)
    
    with transform(CENTER), rotate(90):
        arc(x, y, OUTER_RADIUS, range= prog_amount, fill=None,
            stroke=0.6, strokewidth=STROKE_WIDTH)

def topic_progress(x,y, **kwargs):
    import random
    import icons
    
    
    stroke_width = 5
    outer_radius = 47
    topic_radius = 35
    domain_radius = 38.5
    topic = kwargs.get('topic', None)
    domain = kwargs.get('domain', 'math')
    use_image = kwargs.get('image', True)

    progs = sorted([int(random.uniform(5, 95)) for a in range(4)],
                    lambda b,c: c-b) # sort descending
    print '%d%% mastered' % progs[-1] # mastery percentage
    colors = [color(z) for z in ['#9bdbea', # practiced
                                '#57c3dc', # mastery 1
                                '#28aac9', # mastery 2
                                '#1b7489']] # mastered
    
    # draw grey circle which others overlay atop
    arc(x, y, outer_radius, range=360, fill=None, stroke='#dedede', strokewidth=stroke_width)    
    icon_radius = 128
    # image is 128 but we will use it at different size to match inner topic radius
    scaling = topic_radius * 2 / 128.0
    if use_image and topic and icons.get_icon_for(topic, []):
        with translate(x-icon_radius/2,y-icon_radius/2), scale(scaling):
            with clip(oval(0,0,icon_radius,icon_radius)):
                image("~/khan/webapp%s" % icons.get_icon_for(topic, []))
    else:
        # arc(x, y, topic_radius, range=360, fill=subject_color_for(domain))
        # draw background disc of topic color for image
        # arc(x, y, domain_radius, range=360, fill=topic_color_for(domain))

        font("Proxima Nova", "Regular", 24)
        align(CENTER)
        text("%d%%" % (progs[-2]), x+3, y+4, fill=domain_color_for(domain))
        font("Proxima Nova", "Regular", 12)
        align(CENTER)
        text("progress", x+3, y+18, fill=domain_color_for(domain))


    for c, p in zip(colors, progs):
        amount = p * 360.0 / 100.0
        with transform(CENTER), rotate(90):
            arc(x, y, outer_radius, range=amount, fill=None, stroke=c, strokewidth=stroke_width)

# get a random topic
sl = get_topics(domain='math')[0]['slug']
topic_progress(200, 200, topic=sl, domain='math', image=False)


# progress(50,50)

def topic_display(**kwargs):
    import icons
    reload(icons)

    domain = kwargs.get("domain", "math")
    subject = kwargs.get("subject", 'cc-seventh-grade-math')
    max_y = 40
    for i, t in enumerate(get_topics(domain=domain, subject=subject)):
        heading_y = max_y
        fill(domain_color_for(domain))
        # the topic heading
        text("%s" % t['title'], 40, heading_y, style="subjecthead")
        
        ancestors = [subject, domain]
        icon = icons.get_icon_for(t['slug'], ancestors)

        with translate(-75, heading_y - 68):
            with scale(.25):
                with clip(oval(0,0,128,128)):
                    image("~/khan/webapp%s" % icon)
        
        fill(.6)
        desc = text(t['description'], 40, heading_y + 30, style="subject", width=600, leading=1)
        heading_y += measure(desc).height + 20
        
        maxes = [heading_y + 70 + (50 * len(c['children'])) for c in t['children']]
        for j, tut in enumerate(t['children']):
            tutorial_x = 40 + j * 280
            fill(.4)

            strokewidth(1)
            stroke(.6)
            line(tutorial_x + 10, heading_y+70 - 10, tutorial_x + 10, heading_y + 70 + 50 * (len(tut['children'])-1))
            
            # tutorial title
            fill(subject_color_for(domain))
            text(tut['title'], tutorial_x, heading_y + 30, style="subject", width=240, height=40)
            for k, content in enumerate(tut['children']):
                fill(.6)
                content_y = heading_y + 70 + 50 * k

                # content title
                oval(tutorial_x, content_y-17, 20, 20)
                fill(domain_color_for(domain))
                text(content['title'], tutorial_x + 30, content_y, style="subject", 
                    width=220, height=50, leading=1.1)

        max_y = max(maxes)
        max_y += 75

## draw a topic tree for a given subject 
# with translate(100, 0):
#     topic_display()


def topic_icons(**kwargs):
    import icons
    import random
    domain_slugs = [t['slug'] for t in domains[1:]]
    domain_slug = kwargs.get('domain', random.choice(domain_slugs))
    # domain_title = TODODODODODODO
    
    subject_slugs = [s['slug'] for s in subjects_for_domain(domain_slug)]
    subject_slug = kwargs.get('subject', random.choice(subject_slugs))
    # subject_title = TODODODODODODODO

    topic_names = [t['slug'] for t in get_topics(domain=domain_slug, subject=subject_slug)]
    ancestors = [subject_slug, domain_slug]
    paths = [icons.get_icon_for(t, ancestors) for t in topic_names]
    paths = filter(lambda x: x, paths)
    return [image('~/khan/webapp%s'%p, plot=None) for p in paths]

# print topic_icons()
