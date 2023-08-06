# -*- coding: utf-8 -*-

"""Reproducibly/automatically download data from the DepMap."""

from .api import (  # noqa:F401
    crispr_gene_dependencies_url,
    ensure_achilles_gene_dependencies,
    ensure_crispr_gene_dependencies,
    get_achilles_gene_dependencies_url,
)
