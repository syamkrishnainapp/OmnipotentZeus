# Prometheus creates the database that will house all data. It is currently designed with a MySQL database engine.
from conf import *
from sqlalchemy import MetaData, Column, Integer, String, Float, create_engine, __version__
from sqlalchemy.ext.declarative import declarative_base

# Check which version of SQLAlchemy is currently being used.
print "Current SQLAlchemy Version: " + __version__
Base = declarative_base()
metadata = MetaData()


class Olympus(Base):
    __tablename__ = 'olympus'
    id = Column(Integer, primary_key=True)
    project = Column(String(30), nullable=False)
    uid = Column(String(50), nullable=False)
    provider = Column(String(30), nullable=False)
    region = Column(String(30), nullable=False)
    startdate = Column(String(30), nullable=False)
    iteration = Column(Integer, nullable=False)
    iteration_start_time = Column(String(50), nullable=False)
    processor = Column(String(100), nullable=True)
    vm = Column(String(30), nullable=False)
    vmcount = Column(Integer, nullable=False)
    vcpu = Column(Integer, nullable=False)
    ram = Column(Float(30), nullable=False)
    local = Column(Integer, nullable=False)
    block = Column(Integer, nullable=False)
    disk_rand = Column(String(10), nullable=True)
    disk_seq = Column(String(10), nullable=True)
    disk_blocksize = Column(String(20), nullable=True)
    disk_filesize = Column(String(20), nullable=True)
    disk_numjobs = Column(String(20), nullable=True)
    disk_direct = Column(String(20), nullable=True)
    runtime = Column(Float(30), nullable=True)
    intmulti = Column(Integer, nullable=True)
    floatmulti = Column(Integer, nullable=True)
    memmulti = Column(Integer, nullable=True)
    intsingle = Column(Integer, nullable=True)
    floatsingle = Column(Integer, nullable=True)
    memsingle = Column(Integer, nullable=True)
    totalmulti = Column(Integer, nullable=True)
    totalsingle = Column(Integer, nullable=True)
    aes = Column(Float(30), nullable=True)
    twofish = Column(Float(30), nullable=True)
    sha1 = Column(Float(30), nullable=True)
    sha2 = Column(Float(30), nullable=True)
    bzipcompression = Column(Float(30), nullable=True)
    bzipdecompression = Column(Float(30), nullable=True)
    jpegcompression = Column(Float(30), nullable=True)
    jpegdecompression = Column(Float(30), nullable=True)
    pngcompression = Column(Float(30), nullable=True)
    pngdecompression = Column(Float(30), nullable=True)
    sobel = Column(Float(30), nullable=True)
    lua = Column(Float(30), nullable=True)
    dijkstra = Column(Float(30), nullable=True)
    blackscholes = Column(String(50), nullable=True)
    mandelbrot = Column(Float(30), nullable=True)
    sharpenimage = Column(Float(30), nullable=True)
    blurimage = Column(Float(30), nullable=True)
    sgemm = Column(Float(30), nullable=True)
    dgemm = Column(Float(30), nullable=True)
    sfft = Column(Float(30), nullable=True)
    dfft = Column(Float(30), nullable=True)
    nbody = Column(Float(30), nullable=True)
    raytrace = Column(Float(30), nullable=True)
    copy = Column(Float(30), nullable=True)
    scale = Column(Float(30), nullable=True)
    add = Column(Float(30), nullable=True)
    triad = Column(Float(30), nullable=True)
    runtime_read_seq = Column(Float(30), nullable=True)
    runtime_write_seq = Column(Float(30), nullable=True)
    io_read_seq = Column(Float(30), nullable=True)
    io_write_seq = Column(Float(30), nullable=True)
    iops_read_seq = Column(Float(30), nullable=True)
    iops_write_seq = Column(Float(30), nullable=True)
    bw_read_seq = Column(Float(30), nullable=True)
    bw_write_seq = Column(Float(30), nullable=True)
    iops_read_100_seq = Column(Float(30), nullable=True)
    iops_write_100_seq = Column(Float(30), nullable=True)
    throughput_read_100_seq = Column(Float(30), nullable=True)
    throughput_write_100_seq = Column(Float(30), nullable=True)
    lat_read_100_seq = Column(Float(30), nullable=True)
    lat_write_100_seq = Column(Float(30), nullable=True)
    runtime_read_seq_async = Column(Float(30), nullable=True)
    runtime_write_seq_async = Column(Float(30), nullable=True)
    io_read_seq_async = Column(Float(30), nullable=True)
    io_write_seq_async = Column(Float(30), nullable=True)
    iops_read_seq_async = Column(Float(30), nullable=True)
    iops_write_seq_async = Column(Float(30), nullable=True)
    bw_read_seq_async = Column(Float(30), nullable=True)
    bw_write_seq_async = Column(Float(30), nullable=True)
    iops_read_100_seq_async = Column(Float(30), nullable=True)
    iops_write_100_seq_async = Column(Float(30), nullable=True)
    throughput_read_100_seq_async = Column(Float(30), nullable=True)
    throughput_write_100_seq_async = Column(Float(30), nullable=True)
    lat_read_100_seq_async = Column(Float(30), nullable=True)
    lat_write_100_seq_async = Column(Float(30), nullable=True)
    runtime_read_rand = Column(Float(30), nullable=True)
    runtime_write_rand = Column(Float(30), nullable=True)
    io_read_rand = Column(Float(30), nullable=True)
    io_write_rand = Column(Float(30), nullable=True)
    iops_read_rand = Column(Float(30), nullable=True)
    iops_write_rand = Column(Float(30), nullable=True)
    bw_read_rand = Column(Float(30), nullable=True)
    bw_write_rand = Column(Float(30), nullable=True)
    iops_read_100_rand = Column(Float(30), nullable=True)
    iops_write_100_rand = Column(Float(30), nullable=True)
    throughput_read_100_rand = Column(Float(30), nullable=True)
    throughput_write_100_rand = Column(Float(30), nullable=True)
    lat_read_100_rand = Column(Float(30), nullable=True)
    lat_write_100_rand = Column(Float(30), nullable=True)
    runtime_read_rand_async = Column(Float(30), nullable=True)
    runtime_write_rand_async = Column(Float(30), nullable=True)
    io_read_rand_async = Column(Float(30), nullable=True)
    io_write_rand_async = Column(Float(30), nullable=True)
    iops_read_rand_async = Column(Float(30), nullable=True)
    iops_write_rand_async = Column(Float(30), nullable=True)
    bw_read_rand_async = Column(Float(30), nullable=True)
    bw_write_rand_async = Column(Float(30), nullable=True)
    iops_read_100_rand_async = Column(Float(30), nullable=True)
    iops_write_100_rand_async = Column(Float(30), nullable=True)
    throughput_read_100_rand_async = Column(Float(30), nullable=True)
    throughput_write_100_rand_async = Column(Float(30), nullable=True)
    lat_read_100_rand_async = Column(Float(30), nullable=True)
    lat_write_100_rand_async = Column(Float(30), nullable=True)
    internal_network_data = Column(Float(30), nullable=True)
    internal_network_bandwidth = Column(Float(30), nullable=True)
    hostname = Column(String(100), nullable=True)
    concurrency_level = Column(Integer, nullable=True)
    completed_requests = Column(Integer, nullable=True)
    time_taken = Column(Float(30), nullable=True)
    requests_per_sec = Column(Float(30), nullable=True)
    percent_50 = Column(Integer, nullable=True)
    percent_66 = Column(Integer, nullable=True)
    percent_75 = Column(Integer, nullable=True)
    percent_80 = Column(Integer, nullable=True)
    percent_90 = Column(Integer, nullable=True)
    percent_95 = Column(Integer, nullable=True)
    percent_98 = Column(Integer, nullable=True)
    percent_99 = Column(Integer, nullable=True)
    percent_100 = Column(Integer, nullable=True)
    iozone_seq_writers = Column(Float(30), nullable=True)
    iozone_seq_rewriters = Column(Float(30), nullable=True)
    iozone_seq_readers = Column(Float(30), nullable=True)
    iozone_seq_rereaders = Column(Float(30), nullable=True)
    iozone_random_readers = Column(Float(30), nullable=True)
    iozone_random_writers = Column(Float(30), nullable=True)
    sysbench_seq_write = Column(Float(30), nullable=True)
    sysbench_seq_read = Column(Float(30), nullable=True)
    sysbench_rand_write = Column(Float(30), nullable=True)
    sysbench_rand_read = Column(Float(30), nullable=True)
    perlbench_base_copies = Column(String(20), nullable=True)
    perlbench_base_runtime = Column(String(20), nullable=True)
    perlbench_base_rate = Column(String(20), nullable=True)
    perlbench_peak_copies = Column(String(20), nullable=True)
    perlbench_peak_runtime = Column(String(20), nullable=True)
    perlbench_peak_rate = Column(String(20), nullable=True)
    bzip2_base_copies = Column(String(20), nullable=True)
    bzip2_base_runtime = Column(String(20), nullable=True)
    bzip2_base_rate = Column(String(20), nullable=True)
    bzip2_peak_copies = Column(String(20), nullable=True)
    bzip2_peak_runtime = Column(String(20), nullable=True)
    bzip2_peak_rate = Column(String(20), nullable=True)
    gcc_base_copies = Column(String(20), nullable=True)
    gcc_base_runtime = Column(String(20), nullable=True)
    gcc_base_rate = Column(String(20), nullable=True)
    gcc_peak_copies = Column(String(20), nullable=True)
    gcc_peak_runtime = Column(String(20), nullable=True)
    gcc_peak_rate = Column(String(20), nullable=True)
    mcf_base_copies = Column(String(20), nullable=True)
    mcf_base_runtime = Column(String(20), nullable=True)
    mcf_base_rate = Column(String(20), nullable=True)
    mcf_peak_copies = Column(String(20), nullable=True)
    mcf_peak_runtime = Column(String(20), nullable=True)
    mcf_peak_rate = Column(String(20), nullable=True)
    xalancbmk_base_copies = Column(String(20), nullable=True)
    xalancbmk_base_runtime = Column(String(20), nullable=True)
    xalancbmk_base_rate = Column(String(20), nullable=True)
    xalancbmk_peak_copies = Column(String(20), nullable=True)
    xalancbmk_peak_runtime = Column(String(20), nullable=True)
    xalancbmk_peak_rate = Column(String(20), nullable=True)
    soplex_base_copies = Column(String(20), nullable=True)
    soplex_base_runtime = Column(String(20), nullable=True)
    soplex_base_rate = Column(String(20), nullable=True)
    soplex_peak_copies = Column(String(20), nullable=True)
    soplex_peak_runtime = Column(String(20), nullable=True)
    soplex_peak_rate = Column(String(20), nullable=True)
    sphinx3_base_copies = Column(String(20), nullable=True)
    sphinx3_base_runtime = Column(String(20), nullable=True)
    sphinx3_base_rate = Column(String(20), nullable=True)
    sphinx3_peak_copies = Column(String(20), nullable=True)
    sphinx3_peak_runtime = Column(String(20), nullable=True)
    sphinx3_peak_rate = Column(String(20), nullable=True)


# Create an object, db, to act as the connect to the database.
# The SQLEngine object is used to open the connection, which is what is being used in the db variable.
# Format for create_engine is "engine://user:password@host:port/database"
Ignition = create_engine("mysql://%s:%s@%s:3306/%s" % (db_user, db_password, db_host, db_name), pool_recycle=30)

# Holds all the database metadata.
Base.metadata.create_all(Ignition)
