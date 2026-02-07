def Dense(param, activation, kernel_initializer, input_dim):
    pass


def Sequential():
    pass


def define_generator(latent_dim,n_outputs=2):
    model=Sequential()
    model.add(Dense(30,activation='relu',kernel_initializer='he_uniform',input_dim=latent_dim))
    