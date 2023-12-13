using System;
using System.Collections.Generic;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata;

namespace Lab6.Models
{
    public partial class DB_LabsContext : DbContext
    {
        public DB_LabsContext()
        {
        }

        public DB_LabsContext(DbContextOptions<DB_LabsContext> options)
            : base(options)
        {
        }

        public virtual DbSet<Employee> Employees { get; set; } = null!;
        public virtual DbSet<Engine> Engines { get; set; } = null!;
        public virtual DbSet<Feature> Features { get; set; } = null!;
        public virtual DbSet<Finance> Finances { get; set; } = null!;
        public virtual DbSet<Light> Lights { get; set; } = null!;
        public virtual DbSet<Log> Logs { get; set; } = null!;
        public virtual DbSet<Mark> Marks { get; set; } = null!;
        public virtual DbSet<Model> Models { get; set; } = null!;
        public virtual DbSet<Order> Orders { get; set; } = null!;
        public virtual DbSet<OrderStatus> OrderStatuses { get; set; } = null!;
        public virtual DbSet<Product> Products { get; set; } = null!;
        public virtual DbSet<ProductStatus> ProductStatuses { get; set; } = null!;
        public virtual DbSet<Review> Reviews { get; set; } = null!;
        public virtual DbSet<User> Users { get; set; } = null!;
        public virtual DbSet<Wheel> Wheels { get; set; } = null!;

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            if (!optionsBuilder.IsConfigured)
            {
                optionsBuilder.UseNpgsql("Host=localhost;Database=DB_Labs;Username=postgres;Password=336314010");
            }
        }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<Employee>(entity =>
            {
                entity.ToTable("employee");

                entity.HasIndex(e => e.HireDate, "employee_hire_date");

                entity.Property(e => e.Id).HasColumnName("id");

                entity.Property(e => e.HireDate).HasColumnName("hire_date");

                entity.Property(e => e.UserId).HasColumnName("user_id");

                entity.HasOne(d => d.User)
                    .WithMany(p => p.Employees)
                    .HasForeignKey(d => d.UserId)
                    .HasConstraintName("employee_user_fk");
            });

            modelBuilder.Entity<Engine>(entity =>
            {
                entity.ToTable("engine");

                entity.HasIndex(e => new { e.Name, e.Volume }, "engine_name_volume");

                entity.Property(e => e.Id).HasColumnName("id");

                entity.Property(e => e.Name)
                    .HasColumnType("character varying")
                    .HasColumnName("name");

                entity.Property(e => e.Volume)
                    .HasColumnType("character varying")
                    .HasColumnName("volume");
            });

            modelBuilder.Entity<Feature>(entity =>
            {
                entity.ToTable("feature");

                entity.HasIndex(e => e.Name, "feature_name");

                entity.Property(e => e.Id).HasColumnName("id");

                entity.Property(e => e.Name)
                    .HasColumnType("character varying")
                    .HasColumnName("name");
            });

            modelBuilder.Entity<Finance>(entity =>
            {
                entity.ToTable("finance");

                entity.Property(e => e.Id).HasColumnName("id");

                entity.Property(e => e.Action).HasColumnName("action");

                entity.Property(e => e.Sum).HasColumnName("sum");

                entity.Property(e => e.Time)
                    .HasColumnType("timestamp without time zone")
                    .HasColumnName("time");
            });

            modelBuilder.Entity<Light>(entity =>
            {
                entity.ToTable("light");

                entity.HasIndex(e => e.Name, "light_name");

                entity.Property(e => e.Id).HasColumnName("id");

                entity.Property(e => e.Name)
                    .HasColumnType("character varying")
                    .HasColumnName("name");
            });

            modelBuilder.Entity<Log>(entity =>
            {
                entity.ToTable("log");

                entity.Property(e => e.Id).HasColumnName("id");

                entity.Property(e => e.Action)
                    .HasColumnName("action")
                    .HasComment("1 - entrance || 0 - exit");

                entity.Property(e => e.IdUser).HasColumnName("id_user");

                entity.HasOne(d => d.IdUserNavigation)
                    .WithMany(p => p.Logs)
                    .HasForeignKey(d => d.IdUser)
                    .HasConstraintName("log_user_fk");
            });

            modelBuilder.Entity<Mark>(entity =>
            {
                entity.ToTable("mark");

                entity.HasIndex(e => new { e.Name, e.PlaceOfProduction }, "mark_name_place");

                entity.Property(e => e.Id).HasColumnName("id");

                entity.Property(e => e.Name)
                    .HasColumnType("character varying")
                    .HasColumnName("name");

                entity.Property(e => e.PlaceOfProduction)
                    .HasColumnType("character varying")
                    .HasColumnName("place_of_production");
            });

            modelBuilder.Entity<Model>(entity =>
            {
                entity.ToTable("model");

                entity.HasIndex(e => new { e.Name, e.Year }, "model_name_year");

                entity.Property(e => e.Id).HasColumnName("id");

                entity.Property(e => e.MarkId).HasColumnName("mark_id");

                entity.Property(e => e.Name)
                    .HasColumnType("character varying")
                    .HasColumnName("name");

                entity.Property(e => e.Year).HasColumnName("year");

                entity.HasOne(d => d.Mark)
                    .WithMany(p => p.Models)
                    .HasForeignKey(d => d.MarkId)
                    .OnDelete(DeleteBehavior.ClientSetNull)
                    .HasConstraintName("model_mark_fk");
            });

            modelBuilder.Entity<Order>(entity =>
            {
                entity.ToTable("order");

                entity.Property(e => e.Id).HasColumnName("id");

                entity.Property(e => e.ProductId).HasColumnName("product_id");

                entity.Property(e => e.StatusId).HasColumnName("status_id");

                entity.Property(e => e.Sum).HasColumnName("sum");

                entity.Property(e => e.Time)
                    .HasColumnType("timestamp without time zone")
                    .HasColumnName("time");

                entity.Property(e => e.UserId).HasColumnName("user_id");

                entity.HasOne(d => d.Product)
                    .WithMany(p => p.Orders)
                    .HasForeignKey(d => d.ProductId)
                    .OnDelete(DeleteBehavior.ClientSetNull)
                    .HasConstraintName("order_product_fk");

                entity.HasOne(d => d.Status)
                    .WithMany(p => p.Orders)
                    .HasForeignKey(d => d.StatusId)
                    .OnDelete(DeleteBehavior.ClientSetNull)
                    .HasConstraintName("order_status_fk");

                entity.HasOne(d => d.User)
                    .WithMany(p => p.Orders)
                    .HasForeignKey(d => d.UserId)
                    .OnDelete(DeleteBehavior.ClientSetNull)
                    .HasConstraintName("order_user_fk");
            });

            modelBuilder.Entity<OrderStatus>(entity =>
            {
                entity.ToTable("order_status");

                entity.Property(e => e.Id).HasColumnName("id");

                entity.Property(e => e.Status)
                    .HasColumnName("status")
                    .HasComment("1 - done || 0 - processing");
            });

            modelBuilder.Entity<Product>(entity =>
            {
                entity.ToTable("product");

                entity.Property(e => e.Id).HasColumnName("id");

                entity.Property(e => e.EngineId).HasColumnName("engine_id");

                entity.Property(e => e.ExteriorColor)
                    .HasColumnType("character varying")
                    .HasColumnName("exterior_color");

                entity.Property(e => e.FeatureId).HasColumnName("feature_id");

                entity.Property(e => e.InteriorColor)
                    .HasColumnType("character varying")
                    .HasColumnName("interior_color");

                entity.Property(e => e.InteriorMaterial)
                    .HasColumnType("character varying")
                    .HasColumnName("interior_material");

                entity.Property(e => e.LightId).HasColumnName("light_id");

                entity.Property(e => e.ModelId).HasColumnName("model_id");

                entity.Property(e => e.StatusId).HasColumnName("status_id");

                entity.Property(e => e.WheelId).HasColumnName("wheel_id");

                entity.HasOne(d => d.Engine)
                    .WithMany(p => p.Products)
                    .HasForeignKey(d => d.EngineId)
                    .OnDelete(DeleteBehavior.ClientSetNull)
                    .HasConstraintName("product_engine_fk");

                entity.HasOne(d => d.Light)
                    .WithMany(p => p.Products)
                    .HasForeignKey(d => d.LightId)
                    .OnDelete(DeleteBehavior.ClientSetNull)
                    .HasConstraintName("product_light_fk");

                entity.HasOne(d => d.Model)
                    .WithMany(p => p.Products)
                    .HasForeignKey(d => d.ModelId)
                    .OnDelete(DeleteBehavior.ClientSetNull)
                    .HasConstraintName("product_model_fk");

                entity.HasOne(d => d.Status)
                    .WithMany(p => p.Products)
                    .HasForeignKey(d => d.StatusId)
                    .OnDelete(DeleteBehavior.ClientSetNull)
                    .HasConstraintName("product_status_fk");

                entity.HasOne(d => d.Wheel)
                    .WithMany(p => p.Products)
                    .HasForeignKey(d => d.WheelId)
                    .OnDelete(DeleteBehavior.ClientSetNull)
                    .HasConstraintName("product_wheel_fk");

                entity.HasMany(d => d.Features)
                    .WithMany(p => p.Products)
                    .UsingEntity<Dictionary<string, object>>(
                        "ProductFeature",
                        l => l.HasOne<Feature>().WithMany().HasForeignKey("FeatureId").OnDelete(DeleteBehavior.ClientSetNull).HasConstraintName("product_feature_feature_id_fkey"),
                        r => r.HasOne<Product>().WithMany().HasForeignKey("ProductId").HasConstraintName("product_feature_product_id_fkey"),
                        j =>
                        {
                            j.HasKey("ProductId", "FeatureId").HasName("product_feature_pk");

                            j.ToTable("product_feature");

                            j.IndexerProperty<int>("ProductId").HasColumnName("product_id");

                            j.IndexerProperty<int>("FeatureId").HasColumnName("feature_id");
                        });
            });

            modelBuilder.Entity<ProductStatus>(entity =>
            {
                entity.ToTable("product_status");

                entity.Property(e => e.Id).HasColumnName("id");

                entity.Property(e => e.Status)
                    .HasColumnName("status")
                    .HasComment("1 - in_stock || 0 - not available");
            });

            modelBuilder.Entity<Review>(entity =>
            {
                entity.ToTable("review");

                entity.Property(e => e.Id).HasColumnName("id");

                entity.Property(e => e.Rating).HasColumnName("rating");

                entity.Property(e => e.Text).HasColumnName("text");

                entity.Property(e => e.UserId).HasColumnName("user_id");

                entity.HasOne(d => d.User)
                    .WithMany(p => p.Reviews)
                    .HasForeignKey(d => d.UserId)
                    .HasConstraintName("review_user_fk");
            });

            modelBuilder.Entity<User>(entity =>
            {
                entity.ToTable("user");

                entity.HasIndex(e => e.Email, "user_email_key")
                    .IsUnique();

                entity.HasIndex(e => new { e.Email, e.Login }, "user_email_login");

                entity.HasIndex(e => e.Login, "user_login_key")
                    .IsUnique();

                entity.Property(e => e.Id).HasColumnName("id");

                entity.Property(e => e.Email)
                    .HasColumnType("character varying")
                    .HasColumnName("email");

                entity.Property(e => e.IsStaff).HasColumnName("is_staff");

                entity.Property(e => e.IsSuperuser).HasColumnName("is_superuser");

                entity.Property(e => e.Login)
                    .HasMaxLength(30)
                    .HasColumnName("login");

                entity.Property(e => e.Password)
                    .HasMaxLength(30)
                    .HasColumnName("password");

                entity.Property(e => e.Phone)
                    .HasMaxLength(13)
                    .HasColumnName("phone");
            });

            modelBuilder.Entity<Wheel>(entity =>
            {
                entity.ToTable("wheel");

                entity.HasIndex(e => new { e.Type, e.Size }, "wheel_type_size");

                entity.Property(e => e.Id).HasColumnName("id");

                entity.Property(e => e.Size).HasColumnName("size");

                entity.Property(e => e.Type)
                    .HasColumnType("character varying")
                    .HasColumnName("type");
            });

            OnModelCreatingPartial(modelBuilder);
        }

        partial void OnModelCreatingPartial(ModelBuilder modelBuilder);
    }
}
