import xarray as xarray

def convert_to_xarray(friendlyvars, data):


    # CONVERSION GOES LIKE THIS:
    #---------------------------
    #gitm_bins(array) -> datadict(dict) -> ds(xr.Dataset)

    # Use this gitmvars when converting to xarray. 
    # xarray doesn't like "!" and other special characters
    #xrgitmvars = ['Rho', 'O_3p_', 'O_2', 'N_2', 'N_4s_', 'NO', 'He', 'N_2d_', 'N_2p_', 'H', 'CO_2', 'O_1d_', 'Temperature', 'v_n_east', 'v_n_north', 'v_n_up', 'v_n_up_O_3p_', 'v_n_up_2n_', 'v_n_up_N_2', 'v_n_up_N_4s_', 'v_n_up_NO', 'v_n_up_He', 'O_4_spPlus_', 'NOPlus', 'O_2Plus', 'N_2Plus', 'NPlus', 'O_2dPlus', 'O_2pPlus', 'HPlus', 'HePlus', 'eMinus', 'eTemperature', 'iTemperature', 'v_i_east', 'v_i_north', 'v_i_up']
    dimnames = ['time', 'lon', 'lat', 'alt']

    # Loop through data for conversion to dict
    datadict={}
    for n, name in enumerate(friendlyvars):
        datadict[name] = (dimnames, data[:,n,:,:,:])
    lats, lons, alts  = np.unique(data['latitude']), np.unique(data['longitude']), np.unique(data['altitude'])

    # Convert to xarray
    ds = xr.Dataset(data_vars=datadict,\
                    coords=dict(\
                    time=times,\
                    lon=lons,\
                    lat=lats,\
                    alt=alts))
    del datadict
    return dataxr

def compress_all_vars(path, dataxr, friendlyvars, complevel=6)
    '''
    Uses zlib to compress the datasets. Has multiple levels of 
    encoding compression levels.

    Args
    ---
    path        : string-like
        Deterimines the path for the compressed data to be saved in.
    dataxr      : xarray.Dataset
        Dataset containing GITM output data in question.
    friendlyvars: list
        List of strings that make up the names of the data variables in dataxr
    complevel   : int
        Determines the level of compression. Default is 6. 0 means no compression.
        1 is the least compression. 9 provides the most compression.

    Output
    ---
    compressed_data.nc  : netCDF4 file
        Contains the same data as dataxr but compressed. Deleting dataxr from 
        memory is now reccomended
    '''
    encoding = {}
    for n, name in enumerate (friendlyvars):
        encoding[name] = ({'zlib': True, 'complevel': complevel})
    data.encoding=encoding
    data.to_netcdf('/petastore/phil/GITM/SimStormForSal/example.nc', encoding=encoding)


    return 