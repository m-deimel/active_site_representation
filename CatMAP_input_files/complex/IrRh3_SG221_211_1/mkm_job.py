from catmap import ReactionModel


mkm_file = 'CH4.mkm'

model = ReactionModel(setup_file=mkm_file)

model.output_variables += ['production_rate','consumption_rate','electronic_energy','free_energy','forward_rate_constant','reverse_rate_constant','forward_rate','reverse_rate','rate_control']

model.run()
