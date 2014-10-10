import sys

BAD_LINES = ["--", "Dr Richard Stallman", "President, Free Software Foundation"
    , "51 Franklin St", "Boston MA 02110", "USA", "www.fsf.org  www.gnu.org"
    , "[[[ To any NSA and FBI agents reading my email: please consider    ]]]"
    , "[[[ whether defending the US Constitution against all enemies,     ]]]"
    , "[[[ foreign or domestic, requires you to follow Snowden's example. ]]]"
    , "Skype: No way! That's nonfree (freedom-denying) software."
    , "Use Ekiga or an ordinary phone call."]

def main(argv):
    def should_keep(line):
        return not (line.startswith('    ') or (line.rstrip() in BAD_LINES))

    input_file = argv[0]
    output_file = argv[1]
    
    # Read input.
    f_in = open(input_file, 'r')
    lines = f_in.readlines()
    f_in.close()

    # Make output.
    output = filter(should_keep, lines)
    
    # Write output.
    f_out = open(output_file, 'w')
    f_out.writelines(output)
    f_out.close()

if __name__=="__main__":
    main(sys.argv[1:])
